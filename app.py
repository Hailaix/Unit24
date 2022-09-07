from flask import Flask, render_template, redirect, request, flash
from models import db, connect_db, Pet
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "secretadoption"
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route("/")
def home_page():
    """Home page of adoption agency"""
    pets = Pet.query.all()
    return render_template("home.html", pets=pets)