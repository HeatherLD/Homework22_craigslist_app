#!/usr/bin/env python
#pip install flask
from flask import Flask, json, render_template, request
import os

#create instance of Flask app
app = Flask(__name__)

#decorator
@app.route("/")
def echo_hello():
    return """Furniture for Sale in the Iowa City area:
            Add "all" to the end of the URL above to see all the options! """

@app.route("/all")
def furn_data():
    json_url = os.path.join(app.static_folder,"","craigslistia.json")
    data_json = json.load(open(json_url))

    return render_template('index.html',data=data_json)

if __name__ == "__main__":
    app.run(debug=True)