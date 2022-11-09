from flask import Flask
from config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())


    with app.app_context():
        from flask_app.routes import app_bp
        from flask_app.manage import cli
        app.register_blueprint(app_bp)
        app.register_blueprint(cli)

        from flask_app.models import db
        db.init_app(app)
        # db.create_all()

        return app
