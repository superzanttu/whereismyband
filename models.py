from flask_login import UserMixin
from . import alchemy_db

class User(UserMixin, alchemy_db.Model):
    id = alchemy_db.Column(alchemy_db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = alchemy_db.Column(alchemy_db.String(100), unique=True)
    password = alchemy_db.Column(alchemy_db.String(100))
    name = alchemy_db.Column(alchemy_db.String(1000))
