from flask import Flask, render_template, url_for
from get_artist import *
import random
import os
app = Flask(__name__)

@app.route("/")#This is for testing only
def hello_world():
    #artists = [Justin, Weekend, Taylor]
    random_number = random.randint(0,2)
    return render_template('index.html', artists = artists, random_number = random_number)

if __name__ == '__main__':
    app.run(debug = True, host="0.0.0.0")