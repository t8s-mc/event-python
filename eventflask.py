from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import sqlalchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = "python event project"

@app.route("/")
def home():
    return render_template("index.html")

#THIN HTET SAN (Start)
@app.route("/registeruser")
def registeruser():
    return render_template("registeruser.html")

@app.route("/booking")
def booking():
    return render_template("booking.html")

#I'll PUSH my code in here!

#THIN HTET SAN (End)