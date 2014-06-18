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

    def test_get_activities(self):
        self.fail('NYI')