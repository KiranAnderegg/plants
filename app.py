from flask import Flask, render_template, request, session
from flask_session import Session
import csv
import os

from helpers import login_required, apology
from models import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///plants.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username or not password or not confirmation:
            return apology("invalid username and/or password", 403)
        if password != confirmation:
            return apology("passwords are not the same", 403)

        return redirect("/login")

    else:
        return render_template("register.html")

@app.route("/add plant", methods=["GET", "POST"])
def add_plant():
    pass

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
