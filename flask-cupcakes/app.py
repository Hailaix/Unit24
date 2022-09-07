"""Flask app for Cupcakes"""

from flask import Flask, render_template, redirect
from models import db, connect_db
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "secretadoption"
debug = DebugToolbarExtension(app)

connect_db(app)