__author__ = 'jkruck'
from flask import Flask, redirect, url_for, request, session,abort
from strava import strava_utils
import logging


Flask.get = lambda self, path: self.route(path, methods=['get'])
Flask.put = lambda self, path: self.route(path, methods=['put'])
Flask.post = lambda self, path: self.route(path, methods=['post'])
Flask.delete = lambda self, path: self.route(path, methods=['delete'])

app = Flask(__name__)
client_secret, client_id = strava_utils.get_settings()
app.secret_key = client_secret
redirect_url = "http://127.0.0.1:5000"


def do_token_exchange(code):
    session.permanent = True
    response = strava_utils.get_token(code)
    if 'message' in response and response['message'] == 'Authorization Error':
        abort(401)
    session['token'] = response['access_token']
    athlete = response['athlete']
    session['athlete_id'] = athlete['id']
    session['athlete_name'] = athlete['firstname'] + " " + athlete['lastname']


@app.get('/')
def get_root():
    #Call back from Strava for token exchange.
    if request.args.get('code'):
        do_token_exchange(request.args.get('code'))
        app.logger.debug("%s logged in" % session['athlete_name'])
        return redirect(url_for('static', filename='loggedin.html'))

    return redirect(url_for('static', filename='index.html'))


@app.get('/login')
def login():
    return redirect("%s?client_id=%s&response_type=code&redirect_uri=%s&scope=view_private"
                    % (strava_utils.OAUTH_URL, client_id, redirect_url))


if __name__ == "__main__":

    app.logger.setLevel(logging.DEBUG)
    app.logger.addHandler(logging.FileHandler('strava.log'))
    app.logger.addHandler(logging.StreamHandler())
    app.debug = True
    app.run()
