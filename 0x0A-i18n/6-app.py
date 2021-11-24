#!/usr/bin/env python3
"""Mock logging in
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """Config for languages
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.before_request
def before_request():
    """find a user if any, and set it as a global on flask.g.user
    """
    g.user = get_user(request.args.get('login_as'))


@app.route('/', methods=["GET"], strict_slashes=False)
def index():
    """Return 6-index
    """
    return render_template('6-index.html')


@babel.localeselector
def get_locale():
    """Get locale selector for babel to
    determine the best match with supported languages
    Detect if the incoming request contains locale argument
    and ifs value is a supported locale, return it
    If not or if the parameter is not present,
    resort to the previous default behavior
    """
    my_locale = request.args.get('locale')
    if my_locale:
        sup_lang = my_locale
    elif g.user and g.user['locale'] in app.config['LANGUAGES']:
        sup_lang = g.user['locale']
    else:
        sup_lang = request.accept_languages.best_match(app.config['LANGUAGES'])
    return sup_lang


def get_user(login_as: int):
    """Returns a user dictionary or None if the ID cannot be found
    or if login_as was not passed
    """
    try:
        int(login_as)
    except Exception:
        return None
    return users.get(int(login_as))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
