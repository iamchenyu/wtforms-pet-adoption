from email.policy import default
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    from app import app
    connect_db(app)

DEFAULT_PHOTO_URL = "https://mylostpetalert.com/wp-content/themes/mlpa-child/images/nophoto.gif"


class Pet(db.Model):
    """Create Pet Model"""

    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    breed = db.Column(db.Text, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    photo_url = db.Column(db.Text, nullable=False, default=DEFAULT_PHOTO_URL)
    notes = db.Column(db.Text, nullable=False, default="/")
    availability = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f"{self.breed} {self.species} {self.name} - Availability {self.available}"
