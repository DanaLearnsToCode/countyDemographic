from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__)

@app.route("/")
def render_main():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    return render_template('select.html', state = get_state_options(counties), fact = get_fact(options, counties))

def get_state_options(counties):
    listOfStates = []
    for county in counties:
        if county["State"] not in listOfStates:
            listOfStates.append(county["State"])
    options = ""
    for state in listOfStates:
        options = options + Markup("<option value=\"" + state + "\">" + state + "</option>")
    return options

def get_fact(options, counties):
    funFact = "The population of this state (in 2014) was "
    county_pop = 0
    for county in counties:
        if county["State"] == options:
            county_pop = county_pop + county["Population"]["2014 Population"]
    fun_fact = fun_fact + str(county_pop)
    return fun_fact

if __name__=="__main__":
    app.run(debug=False, port=54321)
