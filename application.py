from flask import Flask, render_template, url_for
from spotify import songs

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html', songs = songs)

if __name__ == '__main__':
    app.run(debug = True)