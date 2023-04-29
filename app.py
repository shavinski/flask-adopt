"""Flask app for adopt app."""

import os

from flask import Flask, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension

from models import connect_db, db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", "postgresql:///adopt")

connect_db(app)

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

@app.get("/")
def show_homepage():
    """Display homepage"""

    pets = Pet.query.all()

    return render_template("home.html", pets=pets)

@app.route("/add", methods=['GET', 'POST'])
def add_pet():
    """ Handles getting the add route and the form validation for adding a pet """

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data 
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data 
        notes = form.notes.data 
        available = form.available.data

        pet = Pet(
            name=name, 
            species=species, 
            photo_url=photo_url, 
            age=age, 
            notes=notes, 
            available=available)

        db.session.add(pet)
        db.session.commit()

        flash(f"Added {name} the {species} to the adoption page")
        return redirect('/')

    else:
        return render_template(
            "add-pet-form.html", form = form)

@app.route("/<int:pet_id>", methods=["GET", "POST"])
def edit_pet_info(pet_id):
    """Displays page of single pet and optional form to edit pet info"""

    form = EditPetForm()
    pet = Pet.query.get_or_404(pet_id)
    
    if form.validate_on_submit():
        photo_url = form.photo_url.data 
        notes = form.notes.data 
        available = form.available.data

        pet.photo_url = photo_url
        pet.notes = notes
        pet.available = available

        db.session.add(pet)
        db.session.commit()

        flash(f"Edited {pet.name} the {pet.species}")
        return redirect(f'/{pet_id}')

    else:
        return render_template(
            "pet-info.html", form = form, pet = pet)