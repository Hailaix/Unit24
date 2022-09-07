
from models import db, Pet
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
Pet.query.delete()

p1 = Pet(name="Mr. Meow", species="cat", age=10, notes="No real notes")
p2 = Pet(name="fluffy", species="rabbit", age=2)
p3 = Pet(name="Dog", species="dog", age=4, available=False)

db.session.add(p1)
db.session.add(p2)
db.session.add(p3)

db.session.commit()