import datetime
from flask import Flask, render_template, request
from pymongo import MongoClient

def create_app():

    app = Flask(__name__)
    client = MongoClient("mongodb+srv://yashshah3010:ydshah3010@microblog-application-f.ppz5l.mongodb.net/test?authSource=admin&replicaSet=atlas-i3o3cx-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true")
    app.db = client.microblog


    @app.route('/', methods=["GET", "POST"])
    def index():
        if request.method == "POST":
            entry_content = request.form.get("content")
            reader_date = datetime.datetime.today().strftime("%d-%m-%Y")
            formatted_date = datetime.datetime.strptime(reader_date, "%d-%m-%Y").strftime("%b %d")
            app.db.entries.insert_one({"content" : entry_content, "date" : formatted_date, "reader_date" : reader_date})

        return render_template('index.html', entries=app.db.entries.find({}))

    return app 


app = create_app()
app.run(port=5000)