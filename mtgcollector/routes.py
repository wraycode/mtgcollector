
from flask import render_template, url_for, flash, redirect, request
from mtgcollector import app
from mtgcollector.forms import RegistrationForm, LoginForm, CardSearchForm
from mtgcollector.models import User, Post
import json
import requests


posts = [
    {
        'author':'Jeremy Barton',
        'title':'Blog Post 1',
        'content':'First post content',
        'date_posted':'April 20, 2018',
    },
    {
        'author':'Jane Doe',
        'title':'Blog Post 2',
        'content':'Second post content',
        'date_posted':'April 21, 2018',
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f' Account created for {form.username.data}', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'wraycode@gmail.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/mtg/card/", methods=['GET', 'POST'])
def getCardByName(name='Daybreak Chaplain'):
    name='Daybreak Chaplain'
    form = CardSearchForm()
    if form.search.data != "":
        name = form.search.data

    r = requests.get("https://api.scryfall.com/cards/named?fuzzy=Daybreak Chaplain")
    parsed_json = json.loads(r.text)
    return render_template('cards.html', title='cards', form=form, card=parsed_json)

    # todo autocomplete


@app.route("/mtg/card/autocomplete", methods=['GET', 'POST'])
def getCardNamesAutoComplete(name='Daybreak'):

    r = requests.get("https://api.scryfall.com/cards/autocomplete?q="+name)
    return r.text
    #parsed_json = json.loads(r.text)
    #return parsed_json
