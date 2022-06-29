# Flask
from flask import Flask
from flask import request
from flask import session
from flask import abort, redirect, url_for

# Database
import sqlite3
from flask import g
DATABASE = "./database/wimb.db"

# Calendar
import calendar

app = Flask(__name__)

app.secret_key = b'paskpaskpok'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

@app.route("/")
def index():
    html='<p>Terve, apina!</p>'

    if 'username' in session:
        html+=f'Logged in as {session["username"]}'
    else:
        html+='Et ole kirjautuneena'

    html+='<p><a href="/login">Login</a></p>'
    html+='<p><a href="/logout">Logout</a></p>'
    html+='<p><a href="/nogo_calendar">NoGo Calendar</a></p>'
    html+='<p><a href="/bands">Bands</a></p>'
    html+='<p><a href="/members">Members</a></p>'
    html+='<p><a href="/bandmembers">Band Members</a></p>'
    html+='<p><a href="/nogo_dates">NoGo Dates</a></p>'
    return html

@app.get('/login')
def login_get():
    return show_the_login_form()

@app.post('/login')
def login_post():
    return do_the_login()

@app.route("/logout")
def logout():
    return do_the_logout()

@app.route("/bands")
def bands():
    return list_bands()

@app.route("/members")
def members():
    return list_members()

@app.route("/bandmembers")
def bandmembers():
    return list_bandmembers()

@app.route("/nogo_calendar")
def nogo_calendar():
    return show_nogo_calendar()

@app.route("/nogo_dates")
def nogodates():
    return list_nogodates()

def show_the_login_form():
    html='<form method="post">'
    html+='<label for="uname"><b>Käyttäjä</b></label>'
    html+='<input type="text" placeholder="apinan nimi" name="uname" required>'
    html+='<label for="psw"><b>Salasana</b></label>'
    html+='<input type="password" placeholder="tosi fiksu salasana" name="psw" required>'
    html+='<button type="submit">Sisään</button>'
    html+='<label>'
    html+='<input type="checkbox" checked="checked" name="remember">Muista minut'
    html+='</label>'
    html+='<button type="button" class="cancelbtn">Cancel</button>'
    html+='</form>'
    return html

def do_the_login():
    if request.form['uname'] == "santtu":
        session['username'] = request.form['uname']
        return redirect(url_for('index'))

    else:
        return "<p>Ei käy</p>"

def do_the_logout():
    session.pop('username', None)
    return redirect(url_for('index'))

def list_bands():
    html="<h1>Bändit</h1>"
    html+="<table><tr><th>Lyhyt nimi</th><th>Nimi</th></tr>"
    for band in query_db('select * from bands'):
        html += "<tr><td>%s</td><td>%s</td></tr>" % (band['name'], band['name_full'])
    html+="</table>"
    return html

def list_members():
    html="<h1>Jäsenet</h1>"
    html+="<table><tr><th>Lyhyt nimi</th><th>Nimi</th></tr>"
    for band in query_db('select * from members'):
        html += "<tr><td>%s</td><td>%s</td></tr>" % (band['name'], band['name_full'])
    html+="</table>"
    return html

def list_bandmembers():
    html="<h1>Bändien jäsenet</h1>"
    for band in query_db('select * from bands'):
        html+="<h1>%s / %s</h1>" % (band["name"],band["name_full"])
        html+="<table><th>Nimi</th></tr>"

        sql='SELECT * FROM band_members WHERE band_name="%s"' % (band["name"])
        for band_member in query_db(sql):
            html+="<tr><td>%s</td></tr>" % (band_member['member_name'])
        html+="</table>"
    return html

def list_nogodates():
    html="<h1>Ei käy-päivät</h1>"
    html+="<table><tr><th>Päivä</th><th>Jäsen</th></tr>"
    for ngd in query_db('select * from nogo_dates'):
        html += "<tr><td>%s</td><td>%s</td></tr>" % (ngd['date'], ngd['member_name'])
    html+="</table>"
    return html

def show_nogo_calendar():
    #cal=calendar.LocaleHTMLCalendar(firstweekday=0,locale="fi_FI.UTF-8")

    #html=cal.formatmonth(2022, 6, withyear=True)

    #html+="<p>c</p>"

    cal=calendar.Calendar(firstweekday=0)
    html="<h1>NoGo-kalenteri</h1>"

    month_names=["Tammikuu","Helmikuu","Maaliskuu","Huhtikuu","Toukokuu","Kesäkuu","Heinäkuu","Elokuu","Syyskuu","Lokakuu","Marraskuu","Joulukuu"]
    day_name=["Maanantai","Tiistai","Keskiviikko","Torstai","Perjantai","Lauantai","Sunnuntai"]
    for year in range (2022,2024):
        html+="<h1>%s<h1>" % (year)
        for month in range (1,13):
            html+="<h2>%s (%s/%s)</h2>" % (month_names[month-1],month,year)
            #for i in cal.monthdatescalendar(year, month):
            #html+="<p>%s</p>" % (i)
    return html