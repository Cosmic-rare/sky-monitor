from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

from keys import token, uri

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = uri()
db = SQLAlchemy(app)

class Sky(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    pressure = db.Column(db.Integer)
    humidity = db.Column(db.Integer)
    weather_icon = db.Column(db.String(15))
    moon = db.Column(db.Integer)
    year = db.Column(db.Integer)
    month = db.Column(db.Integer)
    day = db.Column(db.Integer)
    time = db.Column(db.Integer)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/archive")
def archive_top():
    return "ar top"

@app.route("/archive/<int:year>")
def archive_year(year):
    return "archive" + str(year)

@app.route("/archive/<int:year>/<int:month>")
def archive_month(year, month):
    return render_template("archive.html", year=year, month=month)

@app.route("/old")
def old():
    return render_template("old.html")

@app.route("/create/<Token>")
def create(Token):
    if Token == token():
        return "<h1>OK</h1>"
    else:
        return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)