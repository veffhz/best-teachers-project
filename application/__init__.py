from flask import Flask
from flask_migrate import Migrate

from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    with app.app_context():
        from . import routes, forms
        from .models import db, Teacher
        db.init_app(app)
        migrate = Migrate()
        migrate.init_app(app, db)
    return app
