import flask


def create_app():
    application = flask.Flask(__name__)
    application.config.from_object('app.settings')
    from app import models
    models.db.init_app(application)
    with application.app_context():
        models.db.create_all()
    return application
