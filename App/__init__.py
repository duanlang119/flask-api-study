from flask import Flask

from App import settings
from App.ext import init_ext


def create_app( env_name ):
    app = Flask(__name__)

    app.config.from_object(settings.config.get(env_name) or "default")

    init_ext(app=app)

    return app
