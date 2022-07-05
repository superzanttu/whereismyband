from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import alchemy_db

main = Blueprint('main', __name__)


# Generates simple menu for develeopers
def get_developer_menu():

    html="<div>"
    html+="<strong>Development menu</strong>: "
    
    devurls=[["show_nogo_calendar","Näytä NoGo-kalenteri"], 
            ["all_bands","Näytä bändit"],
            ["all_members","Näytä käyttäjät"],
            ["all_bandmembers","Näytä bändien jäsenet"],
            ["all_nogo_dates","Näytä kaikki NoGo-päivät listana"],
            ["add_nogo_date","Lisää NoGo-päivä"]]

    for du in devurls:
        html+='<a href="/%s">[%s]</a> ' % (du[0], du[1])
    
    html+="</div>"
    if 'username' in session:
        html+=f'<p>Logged in as {session["username"]}</p>'
    else:
        html+='Et ole kirjautuneena'
    return html


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)


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

