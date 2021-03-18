from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__)

@app.route("/")
def render_main():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    return render_template('select.html', state = get_state_options(counties))

#@app.route("/getState")
def get_state_options(counties):
    listOfStates = []
    for county in counties:
        if not county["State"] in counties:
            listOfStates.append(county["State"])
    print(listOfStates)
    options = ""
    for state in listOfStates:
        options = options + Markup("<option value=\"" + state + "\">" + state + "</option>")
    return options

if __name__=="__main__":
    app.run(debug=False, port=54321)
