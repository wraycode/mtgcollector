from datetime import datetime
from mtgcollector import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist = db.Column(	db.String	nullable=True
    border_color = db.Column( db.String
    collector_number = db.Column( db.String
    digital	= db.Column( db.Boolean
    eur = db.Column(	db.String	nullable=True
    flavor_text = db.Column(	db.String	nullable=True
    frame = db.Column(	db.String
    frame_effect = db.Column(	db.String
    full_art = db.Column(	db.Boolean
    games = db.Column(	db.Array
    highres_image = db.Column(	db.Boolean
    illustration_id = db.Column( db.String()	nullable=True
    image_uris = db.Column(	db.Object	nullable=True
    printed_name = db.Column(	db.String	nullable=True
    printed_text = db.Column(	db.String	nullable=True
    printed_type_line = db.Column(	db.String	nullable=True
    promo = db.Column(	db.Boolean
    purchase_uris = db.Column(	db.Object
    rarity = db.Column(	db.String
    related_uris = db.Column(	db.Object
    released_at = db.Column(	db.Date
    reprint = db.Column(	db.Boolean
    set = db.Column(	db.String
    set_name = db.Column(	db.String
    story_spotlight = db.Column(	db.Boolean
    tix = db.Column(	db.String	nullable=True
    usd = db.Column(	db.String	nullable=True
    watermark = db.Column(	db.String nullable=True

class UserCards
    id = db.Column(db.Integer, primary_key=True)
    user_id
    card_id
