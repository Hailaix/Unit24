from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

def connect_db(app):
    """connect the database to the app"""
    db.app = app
    db.init_app(app)

class User(db.Model):
    """A User"""
    __tablename__ = "users"

    username = db.Column(db.String(20), primary_key=True)
    password = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)

    feedback_list = db.relation('Feedback', backref="user")

    @classmethod
    def register(cls, uname, pwd, email, fname, lname):
        """return a new user (encrypted pwd)"""
        hashpass = bcrypt.generate_password_hash(pwd)
        # Convert from bytestring to utf8 string
        utf8_pass = hashpass.decode("utf8")

        return cls(
            username = uname, 
            password = utf8_pass,
            email = email,
            first_name = fname,
            last_name = lname
            )
    
    @classmethod
    def authenticate(cls, uname, pwd):
        """validate user with database,
        returns user if it exists and the pass is valid, False otherwise
        """
        user = User.query.get(uname)
        if user and bcrypt.check_password_hash(user.password, pwd):
            return user
        return False

class Feedback(db.Model):
    """Some feedback"""
    __tablename__ = "feedback"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    username = db.Column(db.String(20), db.ForeignKey('users.username', ondelete="CASCADE"))