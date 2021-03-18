from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__)

@app.route("/")
def render_main():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    return render_template('base.html')

def get_state_options(counties):
    listOfStates = []
    for county in counties:
        if not county["State"] in counties:
            listOfStates.append(county["State"])
    options = ""
    for state in listOfStates:
        options = options + Markup("<option value=\"" + state + "\">" + state + "</option>")
    return render_template('select.html', state = options, fact = "")

if __name__=="__main__":
    app.run(debug=False, port=54321)
