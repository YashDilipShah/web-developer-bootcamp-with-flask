from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    planets = [
        "Mercury", 
        "Venus", 
        "Earth", 
        "Mother", 
        "Jupiter", 
        "Saturn", 
        "Uranus", 
        "Neptune"
    ]
    return render_template('loops.html', planets=planets, count=5, count2=4, count3=10)

app.run(port=5000)