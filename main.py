import pendulum, datetime
from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import alchemy_db
from dev import get_developer_menu

from .models import User, NoGoDates, Bands, BandMembers

from pprint import pprint 

main = Blueprint('main', __name__)



@main.route('/')
def index():
    return render_template('index.html', devmenu=get_developer_menu() )

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name, devmenu=get_developer_menu())


# URLs for application functions
@main.route ("/all_bands")
@login_required
def url_all_bands():
    return list_all_bands()

@main.route("/all_members")
@login_required
def url_all_members():
    return list_all_members()

@main.route("/all_bandmembers")
@login_required
def url_bandmembers():
    return list_all_band_members()

@main.route("/show_nogo_calendar")
@login_required
def url_show_nogo_calendar():
    return nogo_calendar()

@main.route("/all_nogo_dates")
@login_required
def url_all_nogo_dates():
    return list_all_nogo_dates()

@main.get('/add_nogo_date')
@login_required
def url_add_nogo_get():
    return "ADD NOGO DATE (SHOW FORM)"

@main.post('/add_nogo_date')
@login_required
def url_add_nogo_post():
    return "ADD NOGO DATE"

def list_all_bands():
    stmt = list(alchemy_db.session.execute(alchemy_db.select(Bands)).scalars())
    return render_template('all_bands.html', table_data=stmt, devmenu=get_developer_menu())

def list_all_nogo_dates():
    stmt = list(alchemy_db.session.execute(alchemy_db.select(NoGoDates)).scalars())
    return render_template('all_nogo_dates.html', table_data=stmt, devmenu=get_developer_menu())


def list_all_members():
    stmt = list(alchemy_db.session.execute(alchemy_db.select(User)).scalars())
    return render_template('all_members.html', table_data=stmt, devmenu=get_developer_menu())

def list_all_band_members():
    stmt = list(alchemy_db.session.execute(alchemy_db.select(BandMembers)).scalars())
    return render_template('all_band_members.html', table_data=stmt, devmenu=get_developer_menu())

def nogo_calendar():
    stmt = list(alchemy_db.session.execute(alchemy_db.select(NoGoDates).order_by(NoGoDates.date)).scalars())
    cal={}
    for dd in stmt:
        print("dd:", dd, "dd.date:", dd.date, "type(dd.date):", type(dd.date))
        #ngd = pendulum.from_format(str(dd.date), 'YYYY-MM-DD')
        ngd = pendulum.instance(datetime.datetime.fromordinal(dd.date.toordinal()), tz="Europe/Helsinki")
        print(ngd, type(ngd))
        ngd_year = ngd.year
        ngd_month = ngd.month
        ngd_day = ngd.day

        # print ("Y:",y,"D:",d,"M:",m)
        if ngd_year not in cal.keys():
            cal[ngd_year]={}
            for m in range(1, 12):
                cal[ngd_year][m] = {}
                start_of_month = pendulum.local(ngd_year, m, 1)
                end_of_month = start_of_month.end_of('month')
                cal[ngd_year][m]['first_day'] = start_of_month.day
                cal[ngd_year][m]['first_weekday'] = start_of_month.day_of_week
                cal[ngd_year][m]['last_day'] = end_of_month.day
                for d in range(start_of_month.day, end_of_month.day):
                    cal[ngd_year][m][d]={}
                    cal[ngd_year][m][d]['nogo'] = False
                    cal[ngd_year][m][d]['day'] = d
                    


        #pprint(cal)
                

        #cal[y][w][wd]['nogo'] = True
        #cal[y][w][wd]['year'] = y
        #cal[y][w][wd]['month'] = m
        #cal[y][w][wd]['day'] = d
        #cal[y][w][wd]['day of week'] = wd
        #cal[y][w][wd]['week of year'] = w
        #cal[y][w][wd]['text'] = ngd.format('dddd DD MMMM YYYY')
        

    return render_template('nogo_calendar.html', calendar=cal, devmenu=get_developer_menu())