from flask import Flask, render_template
import random
import hash
import sys
import webbrowser
from data import *

def help():
	webbrowser.open("https://github.com/thebtlgfish/fishapi/blob/main/README.md")



p = sys.argv[1]
app = Flask(__name__)

@app.route("/api")
def index():
	return render_template("index.html")

@app.route("/api/random/quote")
def quote():
	return random.choice(quotes)

@app.route("/api/random/girlname")
def getgirlname():
	return random.choice(girl_names)

@app.route("/api/random/boyname")
def getboyname():
	return random.choice(boy_names)

@app.route('/api/conversion/sha256/<plain_text>', methods=['GET'])
def sha256(plain_text):
	return hash.sha256gen(plain_text)

@app.route("/api/random/joke")
def getrandomjoke():
	return random.choice(jokes)







if p == "--help":
	help()
	sys.exit(0)

app.run(host="0.0.0.0", port=p)
