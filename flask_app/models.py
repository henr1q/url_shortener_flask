from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Urls(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String)
    code = db.Column(db.String(6))
