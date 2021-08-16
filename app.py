from flask import Flask, render_template, redirect

from keys import token

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/archive/<int:year>/<int:month>")
def archive(year, month):
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

app.run(debug=True) 