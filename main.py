from flask import Flask, render_template
import random
from datetime import datetime
from data import *

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/quote")
def quote():
	return random.choice(quotes)

@app.route("/name")
def name():
	return random.choice(names)

@app.route("/time")
def time():
	now = datetime.now()
	current_time = now.strftime("%H:%M:%S")  
	return current_time








app.run(host="0.0.0.0", port=8080)
