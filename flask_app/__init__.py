from flask import Flask
from flask_wtf.csrf import CSRFProtect

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')


    with app.app_context():
        from flask_app.routes import web_bp, api_bp
        from flask_app.manage import cli
        app.register_blueprint(web_bp)
        app.register_blueprint(cli)

        from flask_app.models import db
        db.init_app(app)
        CSRFProtect(app)
        # db.create_all()

        return app
