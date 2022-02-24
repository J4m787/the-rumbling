from msilib.schema import Class

from sqlalchemy import ForeignKey, true
from main import db


class user(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    favourite_id = db.column(db.Integer, ForeignKey=True)





