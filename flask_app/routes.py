from flask import Blueprint, render_template, redirect, url_for
from flask_app.forms import UrlForm
from flask_app.models import db, Urls
import secrets

app_bp = Blueprint('app_bp', __name__)


@app_bp.route('/', defaults={'short_url': None}, methods=['GET', 'POST'])
@app_bp.route('/<short_url>')
def index(short_url):
    form = UrlForm()


    if not short_url:
        return render_template('index.html', form=form)

    # url = db.session.query(Urls).filter_by(code=short_url).first()
    #
    # if url:
    #     return redirect(url.link, code=302)
    # else:
    #     return redirect(url_for('blog_bp.index'))


@app_bp.route('/url_shortener', methods=['GET', 'POST'])
def url_shortener():
    form = UrlForm()

    if form.validate_on_submit():

        long_url = form.url.data
        short_url = secrets.token_urlsafe(4)

        if not long_url.startswith('http') or long_url.startswith('https'):
            long_url = 'http://' + long_url


        url = db.session.query(Urls).filter_by(link=long_url).first()

        if not url:
            new_data = Urls(link=long_url, code=short_url)
            db.session.add(new_data)
            db.session.commit()
        else:
            short_url = url.code

        return render_template('url_shortener.html', form=form, shortened=f'http://127.0.0.1:5000/{short_url}')


    return render_template('url_shortener.html', form=form, shortened=None)