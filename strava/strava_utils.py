__author__ = 'jkruck'

from os import getenv

CLIENT_SECRET = 'CLIENT_SECRET'
CLIENT_ID = 'CLIENT_ID'


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
