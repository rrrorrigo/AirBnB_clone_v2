#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask
from flask import render_template


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


@app.route("/number/<int:n>")
def number(n):
        """display n is a number only if n is an integer"""
        return "{} is a number".format(n)


@app.route("/number_template/<int:n>")
def display(n):
        """display a HTML page only if n is an integer"""
        return render_template("5-number.html", n=n)

@app.route("/number_odd_or_even/<int:n>")
def oddOrEven(n):
        """display a HTML page only if n is an integer"""
        return render_template("6-number_odd_or_even.html", n=n, type="even" if n % 2 == 0 else "odd")

if __name__ == '__main__':
        app.run(host='0.0.0.0', port='5000')
