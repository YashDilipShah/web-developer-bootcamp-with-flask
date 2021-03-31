from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/data-structures/')
def datastructures():
    movies = ["Interstellar", "Tenet", "Shutter Island"]
    return render_template("data_structures.html", movies=movies)

app.run(port=5000)