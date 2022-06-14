from msilib.schema import Class
from sqlalchemy import ForeignKey, true
from main import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash



class User(UserMixin, db.Model):
    __tablename__ = "User"
    id = db.Column(db.Integer, primary_key=True)
    favourite_id = db.Column(db.Integer, ForeignKey('Favourite.id'))
    email = db.Column(db.Text)
    password = db.Column(db.Text)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User{}>'.format(self.email)

class Shoe(db.Model):
    __tablename__ = "Shoe"
    id = db.Column(db.Integer, primary_key=True)
    favourite_id = db.Column(db.Integer, ForeignKey('Favourite.id'))
    silhouettes_id = db.Column(db.Integer, ForeignKey('Silhouette.id'))
    name = db.Column(db.Text)
    description = db.Column(db.Text)
    image = db.Column(db.Text)
    price = db.Column(db.Text)

class Favourite(db.Model):
    __tablename__ = "Favourite"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('User.id'))
    shoe_id = db.Column(db.Integer, ForeignKey('Shoe.id'))

class Silhouette(db.Model):
    __tablename__="Silhouette"
    id = db.Column(db.Integer, primary_key=True)
    brand_id = db.Column(db.Integer, ForeignKey('Brand.id'))
    name = db.Column(db.Text)
    description = db.Column(db.Text)
    image = db.Column(db.Text)

class Brand(db.Model):
    __tablename__ = "Brand"
    id = db.Column(db.Integer, primary_key=True)
    silhouettes_id = db.Column(db.Integer, ForeignKey('Silhouette.id'))
    name = db.Column(db.Text)
    imagename = db.Column(db.Text)