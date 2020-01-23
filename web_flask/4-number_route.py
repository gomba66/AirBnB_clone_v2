#!/usr/bin/python3
"""
This module contains a flask web application
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def display_home():
    """
    Function that print a message when
    the user request for the root of
    the web application
    """
    return("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """
    Function that print a message when
    the user type /hbnb in the web flask
    application.
    """
    return("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def display_txt(text):
    """
    Function that display a message that
    the user wrote.
    """
    return("C " + text.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python(text='is cool'):
    """
    This function display a message that
    the user wrote.
    """
    return("Python " + text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def display_int(n):
    """
    This function only accept integers
    """
    return(str(n) + " is a number")
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
