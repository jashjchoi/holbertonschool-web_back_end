#!/usr/bin/env python3
"""Setup a basic Flask app
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=["GET"], strict_slashes=False)
def index():
    """Return 0-index page
    """
    return render_template('0-index.html')
