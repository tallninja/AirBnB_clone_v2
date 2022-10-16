#!/usr/bin/python3
"""0. Hello Flask!"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """hello hbnb"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """hbnb function"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def url_param(text):
    """url param"""
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route('/python/')
@app.route('/python/<text>', strict_slashes=False)
def python_route(text='is cool'):
    """python route"""
    text = text.replace('_', ' ')
    return f"Python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """number route"""
    if type(n) == int:
        return f"{n} is a number"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
