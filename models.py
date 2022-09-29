from msilib.schema import Class
from sqlalchemy import ForeignKey, true
from main import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship



# Users and Champions association table many-many
UserShoe = db.Table('UserShoe',
    db.Column('id', db.Integer, primary_key=True, nullable=False),
    db.Column('user_id', db.Integer, db.ForeignKey('User.id')),
    db.Column('shoe_id', db.Integer, db.ForeignKey('Shoe.id'))
)


class User(UserMixin, db.Model):
    __tablename__ = "User"
    id = db.Column(db.Integer, primary_key=True)
    favourite_id = db.Column(db.Integer, ForeignKey('Favourite.id'))
    email = db.Column(db.Text)
    password = db.Column(db.Text)
    shoes = db.relationship('Shoe', secondary='UserShoe',
                           back_populates='users')

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User{}>'.format(self.email)


class Brand(db.Model):
    __tablename__ = "Brand"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    silhouettes = db.relationship('Silhouette', back_populates='brand')


class Silhouette(db.Model):
    __tablename__="Silhouette"
    id = db.Column(db.Integer, primary_key=True)
    brand_id = db.Column(db.Integer, ForeignKey('Brand.id'))
    name = db.Column(db.Text)
    description = db.Column(db.Text)
    image = db.Column(db.Text)
    link = db.Column(db.Text)
    shoes = db.relationship('Shoe', back_populates='silhouette')
    brand = db.relationship('Brand', back_populates='silhouettes')


class Shoe(db.Model):
    __tablename__ = "Shoe"
    id = db.Column(db.Integer, primary_key=True)
    silhouette_id = db.Column(db.Integer, ForeignKey('Silhouette.id'))
    name = db.Column(db.Text)
    image = db.Column(db.Text)
    price = db.Column(db.Text)
    silhouette = db.relationship('Silhouette', back_populates='shoes')
    users = db.relationship('User', secondary='UserShoe', back_populates='shoes')
