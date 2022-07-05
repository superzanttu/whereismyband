from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import alchemy_db
from dev import get_developer_menu

main = Blueprint('main', __name__)



@main.route('/')
def index():
    return render_template('index.html', devmenu=get_developer_menu() )

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name, devmenu=get_developer_menu())


# URLs for application functions
@main.route("/all_bands")
@login_required
def url_all_bands():
    return "LIST BANDS"

@main.route("/all_members")
@login_required
def url_all_members():
    return "ALL MEMBERS"

@main.route("/all_bandmembers")
@login_required
def url_bandmembers():
    return "ALL BAND MEMBERS"

@main.route("/show_nogo_calendar")
@login_required
def url_show_nogo_calendar():
    return "SHOW_NOGO_CALENDAR"

@main.route("/all_nogo_dates")
@login_required
def url_all_nogo_dates():
    return "ALL NOGO DATES"

@main.get('/add_nogo_date')
@login_required
def url_add_nogo_get():
    return "ADD NOGO DATE (SHOW FORM)"

@main.post('/add_nogo_date')
@login_required
def url_add_nogo_post():
    return "ADD NOGO DATE"

