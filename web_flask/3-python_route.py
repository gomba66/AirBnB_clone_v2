#!/usr/bin/python3
"""
This module contains a flask web aplication
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def display_home():
    """
    Function that print a message when
    you type the root of the web application
    """
    return("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """
    Function that print a message when
    the user type /hbnb in the web flask application
    """
    return("HBNB")


@app.route('/hbnb/<text>', strict_slashes=False)
def display_txt(text):
    """
    Function that print a message
    using the text of the user
    """
    return("C " + text.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_txt2(text="is cool"):
    """
    Function that print a message
    using the text of the user
    """
    return("Python " + text.replace("_", " "))
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
