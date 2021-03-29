from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template('select.html', options=get_state_options())

@app.route("/stateFacts")
def render_fun_fact():
    state_chosen = request.args['states']
    return render_template('select.html', options=get_state_options(), stateFact=get_fact(state_chosen))

def get_state_options():
    listOfStates = []
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    for county in counties:
        if county["State"] not in listOfStates:
            listOfStates.append(county["State"])
    options = ""
    for state in listOfStates:
        options = options + Markup("<option value=\"" + state + "\">" + state + "</option>")
    return options

def get_fact(state):
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    county_pop = 0
    for county in counties:
        if county["State"] == state:
            county_pop = county_pop + county["Population"]["2014 Population"]
    fun_fact = "The population of" + state + "in 2014 was " + str(county_pop)
    return fun_fact

if __name__=="__main__":
    app.run(debug=False, port=54321)
