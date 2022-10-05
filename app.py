from crypt import methods
from flask import Flask, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet, DEFAULT_PHOTO_URL
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "temp_key"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_adoption'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True


debug = DebugToolbarExtension(app)

connect_db(app)


@app.route("/")
def show_homepage():
    pets = Pet.query.order_by(Pet.id).all()
    return render_template("homepage.html", pets=pets)


@app.route("/add", methods=["GET", "POST"])
def add_pet():
    form = AddPetForm()
    if form.validate_on_submit():
        [name, species, breed, age, photo_url, notes, csrf] = form.data.values()
        if not notes:
            notes = None
        if not photo_url:
            photo_url = None
        pet = Pet(name=name, species=species, breed=breed,
                  age=age, photo_url=photo_url, notes=notes)
        db.session.add(pet)
        db.session.commit()
        flash(f"Pet {name} has been added!", "alert alert-success")
        return redirect("/")
    else:
        return render_template("add_pet_form.html", form=form)


@app.route("/<int:id>", methods=["GET", "POST"])
def edit_pet(id):
    pet = Pet.query.get_or_404(id)
    form = EditPetForm(obj=pet)
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data or DEFAULT_PHOTO_URL
        pet.notes = form.notes.data or "/"
        pet.availability = form.availability.data
        db.session.commit()
        flash(f"Pet {pet.name} has been edited!", "alert alert-success")
        return redirect("/")
    else:
        return render_template("edit_pet_form.html", form=form, pet=pet)
