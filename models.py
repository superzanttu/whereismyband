from flask_login import UserMixin
from . import alchemy_db

class User(UserMixin, alchemy_db.Model):
    __tablename__ = 'members'
    id = alchemy_db.Column(alchemy_db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = alchemy_db.Column(alchemy_db.String(100), unique=True)
    password = alchemy_db.Column(alchemy_db.String(100))
    name = alchemy_db.Column(alchemy_db.String(1000))
    enabled = alchemy_db.Column(alchemy_db.Boolean())

class NoGoCalendar(alchemy_db.Model):
    __tablename__ = 'nogo_dates'
    id = alchemy_db.Column(alchemy_db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    date = alchemy_db.Column(alchemy_db.Date(), nullable=False)
    member_name = alchemy_db.Column(alchemy_db.String(1000), nullable=False)

class Bands(alchemy_db.Model):
    __tablename__ = 'bands'
    id = alchemy_db.Column(alchemy_db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    name = alchemy_db.Column(alchemy_db.String(1000), unique=True, nullable=False)
    full_name = alchemy_db.Column(alchemy_db.String(1000), unique=True, nullable=False)

class BandMembers(alchemy_db.Model):
    __tablename__ = 'band_members'
    id = alchemy_db.Column(alchemy_db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    name = alchemy_db.Column(alchemy_db.String(1000), nullable=False)
    band_name = alchemy_db.Column(alchemy_db.String(1000), nullable=False)

