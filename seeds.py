from models import db, Pet
from app import app

# Create all tables
with app.app_context():
    db.drop_all()
    db.create_all()

# Create pets
chewy = Pet(name="Chewy", species="Dog", breed="Labrador", age=5,
            photo_url="https://cdn.shopify.com/s/files/1/0894/7020/files/Shih-Tzu_480x480.png?v=1622027384", notes="Vaccinated")

mia = Pet(name="Mia", species="Cat", breed="Domestic Short Hair", age=3,
          photo_url="https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/57269701/1/?bust=1662524221&width=1080")

fluffy = Pet(name="Fluffy", species="Rabbit", breed="American Fuzzy Lop", age=0.5,
             photo_url="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Conejillo_de_indias.jpg/250px-Conejillo_de_indias.jpg", notes="Need special care")

db.session.add_all([chewy, mia, fluffy])
db.session.commit()
