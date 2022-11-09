from flask import Blueprint, render_template, redirect, url_for
from flask_app.forms import UrlForm
from flask_app.models import db, Urls
import secrets

web_bp = Blueprint('web_bp', __name__)
api_bp = Blueprint('api_bp', __name__)


@web_bp.route('/', defaults={'short_url': None}, methods=['GET', 'POST'])
@web_bp.route('/<short_url>')
def index(short_url):
    form = UrlForm()

    if short_url:
        url = db.session.query(Urls).filter_by(code=short_url).first()
        if url:
            return redirect(url.link, code=302)
        else:
            return redirect(url_for('web_bp.index'))

    if form.validate_on_submit():
        long_url = form.url.data
        short_url = secrets.token_urlsafe(4)

        if not long_url.startswith('http') and long_url.startswith('https'):
            long_url = 'http://' + long_url

        url = db.session.query(Urls).filter_by(link=long_url).first()

        if not url:
            new_data = Urls(link=long_url, code=short_url)
            db.session.add(new_data)
            db.session.commit()
        else:
            short_url = url.code

        return render_template('index.html', form=form, shortened=f'http://127.0.0.1:5000/{short_url}')

    return render_template('index.html', form=form, shortened=None)


# @api_bp.route('/shorten/<url>', methods=['POST', 'GET'])
# def shorten(url):
#     pass




