import json
import unittest
from os import environ

from nose.tools import raises
from mock import patch
from requests import Response

from strava import strava_utils


class StravaUtilsTestCase(unittest.TestCase):
    expected_client_secret = 'aaabbbccc_is_a_secret'
    expected_client_id = "1234567"

    def setUp(self):
        if 'CLIENT_SECRET' in environ:
            del environ['CLIENT_SECRET']
        if 'CLIENT_ID' in environ:
            del environ['CLIENT_ID']

    @raises(RuntimeError)
    def test_get_settings_fails_with_no_id(self):
        environ['CLIENT_SECRET'] = self.expected_client_secret
        self.assertRaisesRegexp(RuntimeError, 'CLIENT_ID', strava_utils.get_settings())


    @raises(RuntimeError)
    def test_get_settings_fails_with_no_secret(self):
        environ['CLIENT_ID'] = self.expected_client_id
        self.assertRaisesRegexp(RuntimeError, 'CLIENT_SECRET', strava_utils.get_settings())

    def test_get_secret_and_id_reads_from_env_correctly(self):
        environ['CLIENT_SECRET'] = self.expected_client_secret
        environ['CLIENT_ID'] = self.expected_client_id
        secret, client_id = strava_utils.get_settings()
        self.assertEqual(client_id, self.expected_client_id)
        self.assertEqual(secret, self.expected_client_secret)


    @patch('strava.strava_utils.get_settings')
    @patch('requests.post')
    def test_get_token(self, post_mock, settings_mock):
        settings_mock.return_value = self.expected_client_secret, self.expected_client_id
        rv = Response()
        rv.status_code = 200
        post_mock.return_value = rv
        data = '{ "test": "json"}'
        post_mock.return_value._content = data
        response = strava_utils.get_token("12345")
        self.assertEqual(json.loads(data), response)

    def test_days_to_seconds(self):
        self.assertEqual(86400, strava_utils.days_to_seconds(1))
        self.assertEqual(86400 * 2, strava_utils.days_to_seconds(2))
        self.assertEqual(86400 * 111, strava_utils.days_to_seconds(111))

    @patch('requests.get')
    def test_get_activities(self, get_athlete_request):
        get_athlete_request.return_value = self.make_response(200)
        self.assertEqual(json.load(open('data/activities.json')),
                         strava_utils.get_activities_for_user(self.start_date_epoch, 5, "fake_token"))

        get_athlete_request.assert_called_once_with('https://www.strava.com/api/v3/athlete/activities',
                                                    data=self.generated_expected_data())

    @patch('requests.get')
    def test_get_activities_bad_return(self, get_athlete_request):
        get_athlete_request.return_value = self.make_response(500)
        self.assertIsNone(strava_utils.get_activities_for_user(self.start_date_epoch, 5, "fake_token"))
        get_athlete_request.assert_called_once_with('https://www.strava.com/api/v3/athlete/activities',
                                                    data=self.generated_expected_data())

    def generated_expected_data(self):
        expected_data = {"after": self.start_date_epoch,
                         "before": self.start_date_epoch + strava_utils.days_to_seconds(5),
                         "access_token": "fake_token"}
        return expected_data

    def make_response(self, code):
        rv = Response()
        rv.status_code = code
        #This assumes we're running in the test directory. there must be a better way
        rv._content = json.dumps(json.load(open('data/activities.json', 'r')))
        return rv
