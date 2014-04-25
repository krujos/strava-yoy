__author__ = 'jkruck'
from flask import Flask, redirect, url_for, request, session
from strava import strava_utils

Flask.get = lambda self, path: self.route(path, methods=['get'])
Flask.put = lambda self, path: self.route(path, methods=['put'])
Flask.post = lambda self, path: self.route(path, methods=['post'])
Flask.delete = lambda self, path: self.route(path, methods=['delete'])

app = Flask(__name__)
client_secret, client_id = strava_utils.get_settings()
app.secret_key = client_secret


def do_token_exchange(code):
    session.permanent = True
    response = strava_utils.get_token(code)
    session['token'] = response['access_token']
    athlete = response['athlete']
    session['athlete_id'] = athlete['id']
    session['athlete_name'] = athlete['firstname'] + " " + athlete['lastname']


@app.get('/')
def get_root():
    #Call back from Strava for token exchange.
    if request.args.get('code'):
        do_token_exchange(request.args.get('code'))
        return redirect(url_for('static', filename='loggedin.html'))

    return redirect(url_for('static', filename='index.html'))

if __name__ == "__main__":
    app.debug = True
    app.run()
