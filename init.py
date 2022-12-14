#from flask import Blueprint, render_template
#from flask_login import login_required, current_user
#from . import alchemy_db

#from sqlalchemy import Column, ForeignKey, Integer, String
#from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy.orm import relationship
#from sqlalchemy import create_engine

#from msilib import datasizemask

import datetime, pendulum
from flask_login import login_required

from ast import excepthandler
from .models import User, NoGoDates, Bands, BandMembers

from flask import Blueprint
from werkzeug.security import generate_password_hash

from . import alchemy_db, create_app, models;


init = Blueprint('init', __name__)

@init.route('/init')
# @login_required
def init_all():

    try:
        User.__table__.drop(alchemy_db.engine)
    except:
        pass

    try:
        NoGoDates.__table__.drop(alchemy_db.engine)
    except:
        pass

    try:
        Bands.__table__.drop(alchemy_db.engine)
    except:
        pass

    try:
        BandMembers.__table__.drop(alchemy_db.engine)
    except:
        pass






    alchemy_db.create_all(app=create_app());


    # Add test users
    new_user = User(email="santtu@band.com", name="Santtu Salmiakki", password=generate_password_hash("santtu", method='sha256'), developer=True)
    alchemy_db.session.add(new_user)
    new_user = User(email="lipa@band.com", name="Lippa Vika", password=generate_password_hash("lipa", method='sha256'), developer=False)
    alchemy_db.session.add(new_user)
    new_user = User(email="baasi@band.com", name="Basse Bom", password=generate_password_hash("baasi", method='sha256'), developer=False)
    alchemy_db.session.add(new_user)
    new_user = User(email="rumppi@band.com", name="Rane Rump", password=generate_password_hash("rane", method='sha256'), developer=False)
    alchemy_db.session.add(new_user)
    new_user = User(email="kilju@band.com", name="Kille Kilju", password=generate_password_hash("kilju", method='sha256'), developer=False)
    alchemy_db.session.add(new_user)


    # Add test bands
    new_band = Bands(name="KM", full_name="Kaikki mukaan")
    alchemy_db.session.add(new_band)
    new_band = Bands(name="HP", full_name="Hevon Humppa")
    alchemy_db.session.add(new_band)
    new_band = Bands(name="P3", full_name="Paskaa kolmannella")
    alchemy_db.session.add(new_band)
    new_band = Bands(name="LoL", full_name="Lievästi on liukasta")
    alchemy_db.session.add(new_band)

    # Add test users into bands
    new_member = BandMembers(member_id="1", band_id="1")
    alchemy_db.session.add(new_member)
    new_member = BandMembers(member_id="2", band_id="1")
    alchemy_db.session.add(new_member)
    new_member = BandMembers(member_id="3", band_id="1")
    alchemy_db.session.add(new_member)
    new_member = BandMembers(member_id="4", band_id="1")
    alchemy_db.session.add(new_member)
    new_member = BandMembers(member_id="5", band_id="1")
    alchemy_db.session.add(new_member)
    new_member = BandMembers(member_id="1", band_id="2")
    alchemy_db.session.add(new_member)
    new_member = BandMembers(member_id="2", band_id="2")
    alchemy_db.session.add(new_member)
    new_member = BandMembers(member_id="3", band_id="2")
    alchemy_db.session.add(new_member)
    new_member = BandMembers(member_id="1", band_id="3")
    alchemy_db.session.add(new_member)
    new_member = BandMembers(member_id="2", band_id="3")
    alchemy_db.session.add(new_member)
    new_member = BandMembers(member_id="3", band_id="3")
    alchemy_db.session.add(new_member)
    new_member = BandMembers(member_id="4", band_id="4")
    alchemy_db.session.add(new_member)
    new_member = BandMembers(member_id="5", band_id="4")
    alchemy_db.session.add(new_member)

    # Add nogo dates for testing
    nogodate = pendulum.local(2022, 1, 21)
    new_nogo_date = NoGoDates(date=nogodate, member_id=1)
    alchemy_db.session.add(new_nogo_date)
    new_nogo_date = NoGoDates(date=nogodate, member_id=2)
    alchemy_db.session.add(new_nogo_date)
    nogodate = pendulum.local(2022, 1, 25)
    new_nogo_date = NoGoDates(date=nogodate, member_id=1)
    alchemy_db.session.add(new_nogo_date)
    new_nogo_date = NoGoDates(date=nogodate, member_id=2)
    alchemy_db.session.add(new_nogo_date)
    nogodate = pendulum.local(2022, 1, 23)
    new_nogo_date = NoGoDates(date=nogodate, member_id=1)
    alchemy_db.session.add(new_nogo_date)
    new_nogo_date = NoGoDates(date=nogodate, member_id=2)
    alchemy_db.session.add(new_nogo_date)
    nogodate = pendulum.local(2022, 1, 22)
    new_nogo_date = NoGoDates(date=nogodate, member_id=1)
    alchemy_db.session.add(new_nogo_date)
    new_nogo_date = NoGoDates(date=nogodate, member_id=2)
    alchemy_db.session.add(new_nogo_date)
    nogodate = pendulum.local(2022, 1, 5)
    new_nogo_date = NoGoDates(date=nogodate, member_id=1)
    alchemy_db.session.add(new_nogo_date)
    new_nogo_date = NoGoDates(date=nogodate, member_id=2)
    alchemy_db.session.add(new_nogo_date)

    nogodate = pendulum.local(2022, 1, 5)
    new_nogo_date = NoGoDates(date=nogodate, member_id=1)
    alchemy_db.session.add(new_nogo_date)
    new_nogo_date = NoGoDates(date=nogodate, member_id=2)
    alchemy_db.session.add(new_nogo_date)
    nogodate = pendulum.local(2022, 2, 3)
    new_nogo_date = NoGoDates(date=nogodate, member_id=1)
    alchemy_db.session.add(new_nogo_date)
    new_nogo_date = NoGoDates(date=nogodate, member_id=2)
    alchemy_db.session.add(new_nogo_date)

    nogodate = pendulum.local(2022, 2, 2)
    new_nogo_date = NoGoDates(date=nogodate, member_id=3)
    alchemy_db.session.add(new_nogo_date)
    new_nogo_date = NoGoDates(date=nogodate, member_id=4)
    alchemy_db.session.add(new_nogo_date)

    nogodate = pendulum.local(2022, 2, 3)
    new_nogo_date = NoGoDates(date=nogodate, member_id=3)
    alchemy_db.session.add(new_nogo_date)
    new_nogo_date = NoGoDates(date=nogodate, member_id=4)
    alchemy_db.session.add(new_nogo_date)


    nogodate = pendulum.local(2021, 12, 31)
    new_nogo_date = NoGoDates(date=nogodate, member_id=3)
    alchemy_db.session.add(new_nogo_date)
    new_nogo_date = NoGoDates(date=nogodate, member_id=4)
    alchemy_db.session.add(new_nogo_date)

    nogodate = pendulum.local(2022, 1, 1)
    new_nogo_date = NoGoDates(date=nogodate, member_id=3)
    alchemy_db.session.add(new_nogo_date)
    new_nogo_date = NoGoDates(date=nogodate, member_id=4)
    alchemy_db.session.add(new_nogo_date)

    nogodate = pendulum.local(2022, 1, 2)
    new_nogo_date = NoGoDates(date=nogodate, member_id=3)
    alchemy_db.session.add(new_nogo_date)
    new_nogo_date = NoGoDates(date=nogodate, member_id=4)
    alchemy_db.session.add(new_nogo_date)

    nogodate = pendulum.local(2022, 1, 3)
    new_nogo_date = NoGoDates(date=nogodate, member_id=3)
    alchemy_db.session.add(new_nogo_date)
    new_nogo_date = NoGoDates(date=nogodate, member_id=4)
    alchemy_db.session.add(new_nogo_date)

    nogodate = pendulum.local(2021, 12, 30)
    new_nogo_date = NoGoDates(date=nogodate, member_id=3)
    alchemy_db.session.add(new_nogo_date)
    new_nogo_date = NoGoDates(date=nogodate, member_id=4)
    alchemy_db.session.add(new_nogo_date)

    # Commit all changes
    alchemy_db.session.commit()


    return "<p>App initialized</p>"





