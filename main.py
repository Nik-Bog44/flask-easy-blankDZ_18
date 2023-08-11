from flask import Flask
from flask_restx import Api

from setup_db import db
from config import Config
from views.movies import movie_ns


def create_app(config: Config):
    application = Flask(__name__)
    application.config.from_object(config)
    application.app_context().push()

    return application


def configure_app(app: Flask):
    db.init_app(app)
    db.create_all()
    api = Api(app,prefix='/')

    api.add_namespace(movie_ns)


if __name__ == '__main__':
    app = create_app(Config())

    configure_app(app)

    app.run()
