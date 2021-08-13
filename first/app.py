from flask import Flask
from urls import urls
from flask_restful import Api


class DebugConfig(object):
    DEBUG = True
    DEBUG_QUERIES = True


def configure_api(app: Flask):
    api = Api(app)
    for url, resource in urls.items():
        api.add_resource(resource, url)


def create_app(config_class=DebugConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)
    configure_api(app)

    return app
