__author__ = 'jkruck'
from flask import Flask, redirect, url_for
from strava import strava_utils

Flask.get = lambda self, path: self.route(path, methods=['get'])
Flask.put = lambda self, path: self.route(path, methods=['put'])
Flask.post = lambda self, path: self.route(path, methods=['post'])
Flask.delete = lambda self, path: self.route(path, methods=['delete'])

app = Flask(__name__)
#client_secret, client_id = strava_utils.get_settings()
#app.secret_key = client_secret

@app.get('/')
def get_root():
    return redirect(url_for('static', filename='index.html'))

if __name__ == "__main__":
    app.debug = True
    app.run()
