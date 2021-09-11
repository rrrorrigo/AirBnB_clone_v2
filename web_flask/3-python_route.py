#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello():
        """display on route '/' Hello HBNB!"""
        return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
        """display on route '/hbnb' HBNB"""
        return "HBNB"


@app.route("/c/<text>")
def C(text):
        """ followed by the value of the text variable
        (replace underscore _ symbols with a space )C display """
        text = text.replace('_', ' ')
        return "C {}".format(text)


@app.route("/python")
@app.route("/python/<text>")
def Python(text="is cool"):
        """, followed by the value of the text variable
        (replace underscore _ symbols with a space )Python display """
        text = text.replace('_', ' ')
        return "Python {}".format(text)

if __name__ == '__main__':
        app.run(host='0.0.0.0', port='5000')
