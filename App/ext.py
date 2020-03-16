from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

from App.views import init_blue

db = SQLAlchemy()


def init_ext(app):
    db.init_app(app=app)
    # Session(app=app)

    init_blue(app=app)
