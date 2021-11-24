#!/usr/bin/env python3
"""Parametrize templates
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """Config for languages
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@app.route('/', methods=["GET"], strict_slashes=False)
def index():
    """Return 3-index
    """
    return render_template('3-index.html')


@babel.localeselector
def get_locale():
    """Get locale selector for babel to
    determine the best match with supported languages
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])

if __name__ == "__main__":
    app.run(debug=True)
