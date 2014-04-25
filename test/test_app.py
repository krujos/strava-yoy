__author__ = 'jkruck'

import unittest
from mock import patch
#@patch('strava.strava_utils.get_settings', autospec=True, new=lambda x: ('test_secret', 'test_id'))
from os import environ

#Setup the environment variables so the setup code executes. Seems like there should be a
#way to mock with with patch, but I couldent figure it out.
environ['CLIENT_SECRET'] = 'secret'
environ['CLIENT_ID'] = '12334'
import stravayoy


class AppTests(unittest.TestCase):

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