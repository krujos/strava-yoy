import requests

__author__ = 'jkruck'

from os import getenv
import logging

CLIENT_SECRET = 'CLIENT_SECRET'
CLIENT_ID = 'CLIENT_ID'
TOKEN_EXCHANGE_URL = 'https://www.strava.com/oauth/token'
OAUTH_URL = "https://www.strava.com/oauth/authorize"


def get_settings():
    """
    We assume that the environment is going to tell us our client id and the client secret
    @return secret, id
    """
    client_secret = getenv(CLIENT_SECRET)
    client_id = getenv(CLIENT_ID)

    if None == client_id:
        raise RuntimeError("Invalid environment CLIENT_ID is not set")
    elif None == client_secret:
        raise RuntimeError('Invalid environment CLIENT_SECRET is not set')

    return client_secret, client_id


def get_token(code):
    client_secret, client_id = get_settings()
    data = {"client_id": client_id,
            "client_secret": client_secret,
            "code": code}
    response = requests.post(TOKEN_EXCHANGE_URL, data=data)
    logging.info("Login post returned %d" % response.status_code)
    logging.debug(response.json())

    return response.json()


def get_activities_for_user(start_date, duration):
    pass


def days_to_seconds(num_days):
    return 86400 * num_days