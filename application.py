from flask import Flask, render_template, url_for
from get_artist import *

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template(
        'index.html', songs_by_weekend = songs_by_weekend,
        all_pairs = all_pairs, 
        weekend_image = weekend_image
        )

if __name__ == '__main__':
    app.run(debug = True)