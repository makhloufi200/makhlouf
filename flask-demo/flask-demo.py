#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      smail
#
# Created:     01/03/2018
# Copyright:   (c) smail 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import flask
from flask import Flask
app = Flask(__name__)

@app.route("/index")
def home():
    return "Hi there"

@app.route("/hello/<name>")
def sayhello(name):
    return "Hello {}".format(name)


app.run()