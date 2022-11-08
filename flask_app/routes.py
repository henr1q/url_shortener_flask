from flask import Blueprint, render_template
from flask_app.forms import UrlForm
import secrets

app_bp = Blueprint('app_bp', __name__)

def gen_code():
    pass


@app_bp.route('/')
def index():
    form = UrlForm()
    return render_template('index.html', form=form)