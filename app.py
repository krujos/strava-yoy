__author__ = 'jkruck'
from flask import Flask

Flask.get = lambda self, path: self.route(path, methods=['get'])
Flask.put = lambda self, path: self.route(path, methods=['put'])
Flask.post = lambda self, path: self.route(path, methods=['post'])
Flask.delete = lambda self, path: self.route(path, methods=['delete'])

app = Flask(__name__)

@app.get('/')
def hello():
    return 'hello world'


if __name__ == "__main__":
    app.debug = True
    app.run()