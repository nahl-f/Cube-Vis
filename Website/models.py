from . import db
from flask_login import UserMixin

#one to many, one user can have many times
class Time(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    data = db.Column(db.Numeric(precision=10, scale=2))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    #each user must have a different username
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    time = db.relationship('Time')