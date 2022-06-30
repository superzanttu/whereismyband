# Flask
from flask import Flask
from flask import request
from flask import session
from flask import abort, redirect, url_for, flash

# Flask-login
import flask_login
from flask_login import LoginManager

# Database
import sqlite3
from flask import g
DATABASE = "./database/wimb.db"

# Calendar related libraries
import calendar
import datetime


app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)


app.secret_key = b'paskpaskpok'


# Useb by every URL function to to print out HTML code
# Used as simple and stypupid HTML template
def show_page(html):
    html=get_development_html_menu() + html
    return html

# Includes simple menu for development
def get_development_html_menu():

    html="<div>"
    html+="<strong>Development menu</strong>: "
    
    devurls=[["login","Login"],["logout","Logout"],["register","Rekisteröidy"],["show_nogo_calendar","Näytä EiKäy-kalenteri"], ["all_bands","Näytä bändit"], ["all_members","Näytä käyttäjät"],["all_bandmembers","Näytä bändien jäsenet"],["all_nogo_dates","Näytä kaikki EiKäy-päivät"],["add_nogo_date","Lisää EiKäy-päivä"]]

    for du in devurls:
        html+='<a href="/%s">[%s]</a> ' % (du[0], du[1])
    
    html+="</div>"
    if 'username' in session:
        html+=f'<p>Logged in as {session["username"]}</p>'
    else:
        html+='Et ole kirjautuneena'
    return html

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

def query_db_all(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def query_db_one(query, args=(), one=False): # FIXME one=False onkin tarjolla!
    cur = get_db().execute(query, args)
    rv = cur.fetchone()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def write_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = get_db().commit()
    cur.close()
    return 

@app.route("/")
def url_index():
    html='<p>Terve, apina!</p>'

    return show_page(html)

#@app.get('/login')
#def url_login_get():
#    return show_page(show_the_login_form())

@app.route('/login', methods=['GET', 'POST'])
def url_login():
    return do_the_login()

@app.route("/logout")
def url_logout():
    return do_the_logout()

@app.route("/all_bands")
def url_all_bands():
    return show_page(list_bands())

@app.route("/all_members")
def url_all_members():
    return show_page(list_members())

@app.route("/all_bandmembers")
def url_bandmembers():
    return show_page(list_bandmembers())

@app.route("/show_nogo_calendar")
def url_show_nogo_calendar():
    return show_page(show_nogo_calendar())

@app.route("/all_nogo_dates")
def url_all_nogo_dates():
    return show_page(list_nogodates())

@app.get('/add_nogo_date')
def url_add_nogo_get():
    return show_page(show_the_nogo_form())

@app.post('/add_nogo_date')
def url_add_nogo_post():
    return show_page(add_nogo_date())

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



def get_weeknumber(year,month,day):

    #weeknumber=datetime.date(year, month, day).strftime("%W")
    isoyear,isoweek,isoday=datetime.date(year, month, day).isocalendar()

    return isoweek

def do_the_login():
    
    if request.method == 'POST':
        sql='SELECT * FROM members WHERE name="%s"' % (request.form['uname'])
        userdata = query_db_one(sql)

        if userdata != None:
            if request.form['uname'] == userdata['name']: # FIXME salasanan tarkistus puuttuu
                session['username'] = request.form['uname']
                return redirect(url_for('url_index'))
            return "<p>Ei käy sittenkään</p>"
        else:
            return "<p>Käyttäjää ei löydy</p>"
    else:
        return show_the_login_form()
   

    flash('Logged in successfully.')

    return redirect(url_for('url_index'))

    return flask.render_template('login.html', form=form)
    



    sql='SELECT * FROM members WHERE name="%s"' % (request.form['uname'])
    userdata = query_db_one(sql)

    if userdata != None:
        if request.form['uname'] == userdata['name']: # FIXME salasanan tarkistus puuttuu
            session['username'] = request.form['uname']
            return redirect(url_for('url_index'))
        return "<p>Ei käy sittenkään</p>"
    else:
        return "<p>Käyttäjää ei löydy</p>"

def do_the_logout():
    session.pop('username', None)
    return redirect(url_for('url_index'))

def list_bands():
    html="<h1>Bändit</h1>"
    html+="<table><tr><th>Lyhyt nimi</th><th>Nimi</th></tr>"
    for band in query_db_all('select * from bands'):
        html += "<tr><td>%s</td><td>%s</td></tr>" % (band['name'], band['name_full'])
    html+="</table>"
    return html

def list_members():
    html="<h1>Jäsenet</h1>"
    html+="<table><tr><th>Lyhyt nimi</th><th>Nimi</th></tr>"
    for band in query_db_all('select * from members'):
        html += "<tr><td>%s</td><td>%s</td></tr>" % (band['name'], band['name_full'])
    html+="</table>"
    return html

def list_bandmembers():
    html="<h1>Bändien jäsenet</h1>"
    for band in query_db_all('select * from bands'):
        html+="<h1>%s / %s</h1>" % (band["name"],band["name_full"])
        html+="<table><th>Nimi</th></tr>"

        sql='SELECT * FROM band_members WHERE band_name="%s"' % (band["name"])
        for band_member in query_db_all(sql):
            html+="<tr><td>%s</td></tr>" % (band_member['member_name'])
        html+="</table>"
    return html

def list_nogodates():
    html="<h1>Ei käy-päivät</h1>"
    html+="<table><tr><th>Päivä</th><th>Jäsen</th></tr>"
    for ngd in query_db_all('SELECT * FROM nogo_dates ORDER BY date, member_name'):
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
    day_names=["Maanantai","Tiistai","Keskiviikko","Torstai","Perjantai","Lauantai","Sunnuntai"]

    for year in range (2022,2023):
        html+="<h1>%s<h1>" % (year)
        
        for month in range (1,13):
    
            first_day_of_month, days_in_month = calendar.monthrange(year,month)
            html+="<h2>%s (%s/%s)</h2>" % (month_names[month-1],month,year)

            #html+="<p>%s %s</p>" % (first_day_of_month, days_in_month)

            # Kalenterin taulukon otsikko
            html+='<table style="border: 1px solid black;border-collapse: collapse;">'
            html+='<tr>'
            for d in day_names:
                html+='<th style="border: 1px solid black;border-collapse: collapse;">%s</th>' % d
            html+='<th>Viikko</th>'
            html+="</tr>"
            


            html+="<tr>"

         
            # Täytetään vajaa viikko
            weekday_counter=0
            if first_day_of_month != 0: # Jos kuukausi ei ala maanataina
                for i in range(0,first_day_of_month):
                    html+='<td style="border: 1px solid black;border-collapse: collapse;"></td>'
                    weekday_counter+=1

            # Käydään läpi kuukauden päivät
            for day in range(1,days_in_month+1):
                datetext="%04d-%02d-%02d" % (year, month, day)

                sql= "SELECT COUNT(*) AS count FROM nogo_dates WHERE date='%s'" % (datetext)
                nogo=query_db_one(sql)
               
                if nogo['count'] == 0:
                    html+='<td style="border: 1px solid black;border-collapse: collapse;">%s</td>' % (day)
                else:
                    html+='<td bgcolor="black" style="border-collapse: collapse;border: 1px solid black;color:red"><strong>%s</strong></td>' % (day)
            
                weekday_counter+=1
                if weekday_counter>=7:
                    
                    # Lisätään viikko jokaisen rivin alkuun
                    weeknumber=get_weeknumber(year, month, day)
                    html+='<td style="border: 1px solid black;border-collapse: collapse;">%s</td>' % (weeknumber)
                    weekday_counter=0

                    html+="</tr><tr>"
            

            # Täytetään kuukauden viimeinen viikko
            if weekday_counter > 0:
                for i in range(weekday_counter,7):
                    html+='<td style="border: 1px solid black;border-collapse: collapse;"></td>'

                # Lisätään viikko kuukauden viimeiselle riville
                weeknumber=get_weeknumber(year, month, day)
                html+='<td style="border: 1px solid black;border-collapse: collapse;">%s</td>'% (weeknumber)
            

            html+="</tr>"

            html+="</table>"
    return html

def show_the_nogo_form():
    html='<form method="post">'
    html+='<input type="date" name="nogo_date" required />'
    html+='<button type="submit">Lisää EiKäy-päivä</button>'
    html+='<button type="button" class="cancelbtn">Ei sittenkään</button>'
    html+='</form>'
    return html

def add_nogo_date():

    # Tarkistetaan ettei samaa päivää lisätä uudelleen
    sql='SELECT * FROM nogo_dates WHERE date="%s" AND member_name="%s"  

    sql='INSERT INTO nogo_dates (date, member_name) VALUES ("%s","%s");' % (request.form['nogo_date'], session['username'])
    app.logger.debug (sql)
    userdata = write_db(sql)


    return "<p>Käyttäjälle %s lisätty EiKäy-päivä %s</p>" % (session['username'], request.form['nogo_date'])

class User(flask_login.UserMixin):
    pass
    

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

