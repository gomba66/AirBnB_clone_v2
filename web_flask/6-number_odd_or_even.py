#!/usr/bin/python3
"""
This module contains a flask web application
"""
from flask import Flask
from flask import render_template
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


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_int_temp(n):
    """
    This function that shows a template
    with the variable of the user.
    """
    return(render_template('5-number_template.html', t=n))


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def display_int_odd_or_even(n):
    """
    This function that shows a template
    with the variable of the user.
    """
    return(render_template('6-number_odd_or_even.html', t=n))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
