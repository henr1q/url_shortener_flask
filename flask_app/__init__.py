from flask import Flask
import config


def create_app():
    app = Flask(__name__)
    app.config.from_object(config.Config)

    from flask_app.routes import app_bp
    app.register_blueprint(app_bp)

    return app
