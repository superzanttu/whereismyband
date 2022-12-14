from flask_login import UserMixin
from . import alchemy_db

class User(UserMixin, alchemy_db.Model):
    __tablename__ = 'members'
    id = alchemy_db.Column(alchemy_db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = alchemy_db.Column(alchemy_db.String(100), unique=True)
    password = alchemy_db.Column(alchemy_db.String(100))
    name = alchemy_db.Column(alchemy_db.String(1000))
    enabled = alchemy_db.Column(alchemy_db.Boolean())
    developer = alchemy_db.Column(alchemy_db.Boolean())
    
    @property
    def is_developer(self):
        return True #FIXME

    def __repr__(self):
        return f"User(id={self.id!r}, email={self.email!r}, password={self.password!r}, name={self.name!r}, enabled={self.enabled!r}, developer={self.developer!r})"

class NoGoDates(alchemy_db.Model):
    __tablename__ = 'nogo_dates'
    id = alchemy_db.Column(alchemy_db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    date = alchemy_db.Column(alchemy_db.Date(), nullable=False)
    member_id = alchemy_db.Column(alchemy_db.Integer, nullable=False)

    def __repr__(self):
        return f"NoGoDates(id={self.id!r}, date={self.date!r}, member_id={self.member_id!r})"

class Bands(alchemy_db.Model):
    __tablename__ = 'bands'
    id = alchemy_db.Column(alchemy_db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    name = alchemy_db.Column(alchemy_db.String(1000), unique=True, nullable=False)
    full_name = alchemy_db.Column(alchemy_db.String(1000), unique=True, nullable=False)

    def __repr__(self):
        return f"Bands(id={self.id!r}, name={self.name!r}, full_name={self.full_name!r})"

class BandMembers(alchemy_db.Model):
    __tablename__ = 'band_members'
    id = alchemy_db.Column(alchemy_db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    member_id = alchemy_db.Column(alchemy_db.Integer, nullable=False)
    band_id = alchemy_db.Column(alchemy_db.Integer, nullable=False)

    def __repr__(self):
        return f"BandMembers(id={self.id!r}, member_id={self.member_id!r}, band_id={self.band_id!r})"


