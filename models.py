from msilib.schema import Class
from sqlalchemy import ForeignKey, true
from main import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash



class user(UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    favourite_id = db.Column(db.Integer, ForeignKey('favourite.id'))
    email = db.Column(db.Text)
    password = db.Column(db.Text)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User{}>'.format(self.username)

class shoe(db.Model):
    __tablename__ = "shoe"
    id = db.Column(db.Integer, primary_key=True)
    favourite_id = db.Column(db.Integer, ForeignKey('favourite.id'))
    silhouettes_id = db.Column(db.Integer, ForeignKey('silhouettes.id'))
    name = db.Column(db.Text)
    description = db.Column(db.Text)
    image = db.Column(db.Text)
    price = db.Column(db.Text)

class favourite(db.Model):
    __tablename__ = "favourite"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'))
    shoe_id = db.Column(db.Integer, ForeignKey('shoe.id'))

class silhouette(db.Model):
    __tablename__="silhouette"
    id = db.Column(db.Integer, primary_key=True)
    brands_id = db.Column(db.Integer, ForeignKey('brands.id'))
    name = db.Column(db.Text)
    description = db.Column(db.Text)
    image = db.Column(db.Text)

class brands(db.Model):
    __tablename__ = "brands"
    id = db.Column(db.Integer, primary_key=True)
    silhouettes_id = db.Column(db.Integer, ForeignKey('silhouettes.id'))
    name = db.Column(db.Text)
    imagename = db.Column(db.Text)