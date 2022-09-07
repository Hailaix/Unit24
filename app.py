from flask import Flask, render_template, redirect
from models import db, connect_db, Pet
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddPetForm

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

@app.route("/add", methods=["GET", "POST"])
def add_page():
    """Add pet form"""
    form = AddPetForm()
    if form.validate_on_submit():
        """handle form submission"""
        new_pet = Pet(
            name = form.name.data,
            species = form.species.data,
            photo_url = form.photo_url.data,
            age = form.age.data,
            notes = form.notes.data
        )
        db.session.add(new_pet)
        db.session.commit()
        return redirect("/")
    else:
        return render_template("add.html", form=form)
