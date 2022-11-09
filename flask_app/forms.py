from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_wtf.file import FileField, FileAllowed


class UrlForm(FlaskForm):
    url = StringField("URL", validators=[DataRequired()])
    submit = SubmitField('Shorten URL')