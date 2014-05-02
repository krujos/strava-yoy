__author__ = 'jkruck'

import unittest
from os import environ

from mock import patch
import flask
from flask import Response


#Setup the environment variables so the setup code executes. Seems like there should be a
#way to mock with with patch, but I could not figure it out.
environ['CLIENT_SECRET'] = 'secret'
environ['CLIENT_ID'] = '12334'
import stravayoy


class AppTests(unittest.TestCase):
    athlete = {
        "access_token": "83ebeabdec09f6670863766f792ead24d61fe3f9",
        "athlete": {
            "id": 227615,
            "firstname": "John",
            "lastname": "Applestrava",
            "email": "john@applestrava.com"
        }
    }

    def setUp(self):
        self.app = stravayoy.app.test_client()

    @classmethod
    def tearDownClass(cls):
        del environ['CLIENT_SECRET']
        del environ['CLIENT_ID']

    def test_root_redirects_to_index(self):
        rv = self.app.get('/')
        self.assertEqual(302, rv.status_code, "Was not redirected w/ 302")
        location = rv.headers['Location']
        self.assertTrue(location.endswith('/static/index.html'), "Should have been redirected to /static/index.html")


    @patch('strava.strava_utils.get_token', autospec=True)
    def test_do_token_exchange(self, get_token_mock):
        get_token_mock.return_value = self.athlete
        with stravayoy.app.test_request_context('/&code=12345', method='GET'):
            stravayoy.do_token_exchange("12345")
            get_token_mock.assert_called_once_with("12345")
            self.assertEqual("83ebeabdec09f6670863766f792ead24d61fe3f9", flask.session['token'])

    def test_get_athlete_while_not_logged_in_should_be_unauthroized(self):
        rv = self.app.get('/athlete')
        self.assertEqual(401, rv.status_code)

    def test_get_athlete_logged_in_returns_expected(self):
        with stravayoy.app.test_client() as c:
            with c.session_transaction() as sess:
                sess['athlete_name'] = "John Applestrava"
                sess['athlete_id'] = self.athlete['athlete']['id']
                sess['token'] = self.athlete['access_token']
                resp = c.get('/athlete')
                j = resp.json()
                self.assertEquals("John Applestrava", j['athlete_name'])
                self.assertEquals(227615, j['athlete_id'])

