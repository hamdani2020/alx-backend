#!/usr/bin/env python3
"""
Flask application for translation
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """
    Flask babel configuration
    """
    BABEL_DEFAULT_LOCALE = "en"
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    It retrieves the locale for the web page
    """
    query = request.query_string.decode('utf-8').split('&')
    queryTable = dict(map(
        lambda x: (x if '=' in x else '{}='.format(x)).split('='),
        query,
    ))
    if 'locale' in queryTable:
        if queryTable['locale'] in app.config["LANGUAGES"]:
            return queryTable['locale']
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def get_index() -> str:
    """
    Index page
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(debug=True)
