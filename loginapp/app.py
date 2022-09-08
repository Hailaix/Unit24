from flask import Flask, render_template, redirect, session, flash
from models import db, connect_db, User
from flask_debugtoolbar import DebugToolbarExtension
from forms import RegisterForm, LoginForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///loginapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = "secretlogins"
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route("/")
def index_page():
    """for now, a simple redirect to the register form"""
    return redirect("/register")

@app.route("/register", methods=["GET", "POST"])
def register_page():
    """register form and handler"""
    form = RegisterForm()
    if form.validate_on_submit():
        uname = form.username.data
        pwd = form.password.data
        email = form.email.data
        fname = form.first_name.data
        lname = form.last_name.data
        new_user = User.register(uname, pwd, email, fname, lname)
        db.session.add(new_user)
        try:
            db.session.commit()
        except:
            form.username.errors.append("Username or Email has already been registered")
            return render_template("register_form.html", form=form)

        session["username"] = new_user.username
        
        return redirect(f"/users/{new_user.username}")

    return render_template("register_form.html", form=form)

@app.route("/login", methods=["GET", "POST"])
def login_page():
    """login form and handler"""
    form = LoginForm()
    if form.validate_on_submit():
        uname = form.username.data
        pwd = form.password.data

        user = User.authenticate(uname,pwd)
        if user:
            session["username"] = user.username
            return redirect(f"/users/{user.username}")
        else:
            form.username.errors = ["Invalid username or password"]

    return render_template("login_form.html", form=form)

@app.route("/logout")
def logout():
    """removes the user from the session"""
    session.pop("username")
    return redirect("/")

@app.route("/secret")
def secret_route():
    """the secret page"""
    if "username" not in session:
        flash("You must be logged in to view the secret page", "warning")
        return redirect("/")
    return render_template("secret.html")

@app.route("/users/<username>")
def user_page(username):
    """profile page for the user"""
    if "username" not in session or session["username"] != username:
        flash("You must be logged in as the user to see their profile!", "warning")
        return redirect("/")
    user = User.query.get_or_404(username)
    return render_template("profile.html", user=user)