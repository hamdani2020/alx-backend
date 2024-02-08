#!/usr/bin/env python3
"""
Flask application
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


@app.route('/')
def get_locale() -> str:
    """
    It retrieves the locale for the web page
    """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def get_index() -> str:
    """
    Index page
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)

