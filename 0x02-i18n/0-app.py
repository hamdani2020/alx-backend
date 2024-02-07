#!/usr/bin/env python3
"""
This is a flask application
"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')

def index():
    """
    This function renders the html file index.html
    """
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
