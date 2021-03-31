from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

class GalileanMoons:
    def __init__(self, first, second, third, fourth) -> None:
        self.first = first
        self.second = second 
        self.third = third 
        self.fourth = fourth 

moons = GalileanMoons("Io", "Europa", "Ganymede", "Callisto")


@app.route('/data-structures/')
def data_structures():
    movies = [
        "Interstellar", 
        "Tenet", 
        "The sixth sense"
    ]
    dic = {
        1 : "one", 
        2 : "two"
    }

    kwargs = {
        "movies" : movies, 
        "dic" : dic, 
        "moons" : moons 
    }
    return render_template("data_structures.html", **kwargs)

app.run(port=5000)