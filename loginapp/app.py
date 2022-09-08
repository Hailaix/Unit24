from flask import Flask, render_template, redirect
from models import db, connect_db
from flask_debugtoolbar import DebugToolbarExtension
from forms import RegisterForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "secretlogins"
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route("/")
def index_page():
    """for now, a simple redirect to the register form"""
    return redirect("/register")

@app.route("/register", methods=["GET", "POST"])
def register_page():
    """serves register form and handles registration"""
    form = RegisterForm()
    return render_template("register_form.html", form=form)