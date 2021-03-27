from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template(
        "jinja2.html", name="Yash", template_name="Jinja2")


app.run(debug=True, port=5000)