"""Flask app for adopt app."""

import os

from flask import Flask, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension

from models import connect_db, db, Pet
from forms import AddPetForm

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

@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    """ Handles getting the add route and the form validation for adding a pet """

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data or None
        species = form.species.data or None
        photo_url = form.photo_url.data or None
        age = form.age.data or None
        notes = form.notes.data or None

        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)

        db.session.add(pet)
        db.session.commit()

        flash(f"Added {name} the {species} to the adoption page")
        return redirect('/')

    else:
        return render_template(
            "add-pet-form.html", form = form)


    