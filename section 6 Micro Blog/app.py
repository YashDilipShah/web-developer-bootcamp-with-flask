import datetime
from flask import Flask, render_template, request

app = Flask(__name__)

entries = []

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        entry_content = request.form.get("content")
        formatted_date = datetime.datetime.today().strftime("%d-%m-%Y")
        entries.insert(0, (entry_content, formatted_date))

    entries_with_date = [
        (
            entry[0], 
            entry[1], 
            datetime.datetime.strptime(entry[1], "%d-%m-%Y").strftime("%b %d")
        )
        for entry in entries
    ]
    return render_template('index.html', entries=entries_with_date)

app.run(port=5000)