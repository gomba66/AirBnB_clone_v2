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
    return("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """
    Function that display a message when the
    user request /hbnb in the flask service
    """
    return("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def display_txt(text):
    """
    Function that display a message when the
    user request /hbnb/<text> with the text of
    the user.
    """
    return("C " + text.replace("_", " "))
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
