from flask import Flask, Response
from flask import render_template
from jinja2 import Template
from flask import request
import sqlite3
# import requests
app = Flask(__name__)

DATABASE = 'database.db'
@app.route("/")
def home():
    return render_template('home.html')

@app.route("/about-me")
def aboutMe():
    return render_template('about-me.html')

@app.route("/portfolio")
def portfolio():
    return render_template('portfolio.html')

@app.route("/more-info")
def moreInfo():
    return render_template('more-info.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/content")
def content():
    return render_template('content.html')

if __name__ == "__main__":
    app.run(debug=True)
