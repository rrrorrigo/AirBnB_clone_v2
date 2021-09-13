#!/usr/bin/python3
"""script that starts a Flask web application"""


from models import storage
from models.state import State
from flask import Flask
from flask import render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/states_list")
def stateList():
    """display a HTML page: (inside the tag BODY)"""
    states = storage.all(State)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(exception):
    """removes the current SQLAlchemy session"""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
