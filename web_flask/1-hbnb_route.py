#!/usr/bin/python3
"""0. Hello Flask!"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    """hello hbnb"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """hbnb function"""
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
