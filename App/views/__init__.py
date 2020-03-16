from App.views.views import blue
from .views_user import user


def init_blue(app):
    app.register_blueprint(blueprint=blue)
    app.register_blueprint(blueprint=user)