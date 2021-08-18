from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

from func import request
from keys import token, uri, api

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = uri()
db = SQLAlchemy(app)

class Sky(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    pressure = db.Column(db.Integer)
    humidity = db.Column(db.Integer)
    temp = db.Column(db.Integer)
    weather_icon = db.Column(db.String(15))
    moon = db.Column(db.Integer)
    year = db.Column(db.Integer)
    month = db.Column(db.Integer)
    day = db.Column(db.Integer)
    time = db.Column(db.Integer)


@app.route("/")
def index():
    count = db.session.query(Sky).count()
    data = Sky.query.get(count)
    return render_template("index.html", data=data)

@app.route("/archive")
def archive_top():
    data = db.session.query(Sky.year.distinct().label("year")).order_by("year")
    datas = [row.year for row in data.all()]
    return render_template("ar_top.html", data=datas)

@app.route("/archive/<int:year>")
def archive_year(year):
    data = Sky.query.filter_by(year=year)
    datas = []
    for i in data:
        datas.append(i.month)
    datas = list(set(datas))
    datas.sort()
    print(datas)
    return render_template("archive_year.html", data = datas)

@app.route("/archive/<int:year>/<int:month>")
def archive_month(year, month):
    return render_template("archive.html", year=year, month=month)

@app.route("/old")
def old():
    return render_template("old.html")

@app.route("/create/<Token>")
def create(Token):
    if Token == token():
        data = request("https://api.openweathermap.org/data/2.5/onecall?lon=140.47670066333643&lat=37.759109816261606&units=metric&lang=ja&appid={}".format(api()))
        sky = Sky(
            pressure = data["pressure"],
            humidity = data["humidity"],
            temp = data["temp"],
            weather_icon = data["weather_icon"],
            moon = data["moon"],
            year = data["year"],
            month = data["month"],
            day = data["day"],
            time = data["time"]
        )
        db.session.add(sky)
        db.session.commit()
        return "<h1>書き込めました</h1>"
    else:
        return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)