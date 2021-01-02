from os import path

from flask import Flask
from gevent.pywsgi import WSGIServer
import gevent.monkey
gevent.monkey.patch_all()

from utils import load_plugin

app = Flask(__name__)


def initializer():
    plugins = load_plugin.load_plugins(
        path.join(path.dirname(__file__), 'api'),
        'api'
    )
    for i in plugins:
        app.register_blueprint(i.api)


if __name__ == '__main__':
    initializer()
    http_server = WSGIServer(('0.0.0.0', 10008), app)
    http_server.serve_forever()