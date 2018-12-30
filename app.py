from flask import Flask, render_template, flash, request, redirect, url_for
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import os
import logging

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
logging.basicConfig(filename='usage.log',level=logging.DEBUG)


@app.route("/", methods=['GET', 'POST'])
def index():
	return render_template("index.html")

@app.route("/team", methods=['GET', 'POST'])
def team():
	return render_template("team.html")

@app.errorhandler(404) 
def not_found(e):
	return render_template("404.html")


@app.errorhandler(500)
def application_error(e):
	return 'Sorry, unexpected error: {}'.format(e), 500
 
if(__name__ == "__main__"):
	app.run()
