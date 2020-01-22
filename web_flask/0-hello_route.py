#!/usr/bin/python3
"""
This module contains a flask web inicialization
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def display_r():
    """
    Function that display a message when the flask service is online
    """
    return("Hello HBNB")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
