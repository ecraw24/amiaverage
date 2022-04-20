HEROKU_APP_NAME = "amiaverage"
TABLE_NAME = "skillsinfo"

#import subprocess, psycopg2
#from psycopg2 import sql
from flask import Flask, render_template, current_app, request, url_for
#from flask_sqlalchemy import SQLAlchemy

#This sets up our flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://nvalcjgkjirosy:a1d078c1ef28b3ccb5d5f9ff4583e42243fbd419766d05dacafd70e3dbd79d62@ec2-3-217-251-77.compute-1.amazonaws.com:5432/d4ecfjhp2gbtco"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

'''

#These commands set up our connection to the database
#conn_info = subprocess.run(["heroku", "config:get", "DATABASE_URL", "-a", HEROKU_APP_NAME], stdout = subprocess.PIPE)
#connuri = conn_info.stdout.decode('utf-8').strip()
#conn = psycopg2.connect(connuri)
#cursor = conn.cursor()

#this creates our database object
db = SQLAlchemy(app)

class skillsinfo(db.model):
    __tablename__  = 'skillsinfo'
    id = db.Column(db.Integer, primary_key=True)
    skill_name = db.Column(db.String(50))
    skill_verb = db.Column(db.String(50))
    skill_metric = db.Column(db.String(50))
    unit_of_measurement = db.Column(db.String(50))
    level1 = db.Column(db.Integer)
    level2 = db.Column(db.Integer)
    level3 = db.Column(db.Integer)
    level4 = db.Column(db.Integer)
    level5 = db.Column(db.Integer)

    def __init__(self, skill_name, skill_verb, skill_metric, unit_of_measurement, level1, level2, level3, level4, level5):
        self.skill_name = skill_name
        self.skill_verb = skill_verb
        self.skill_metric = skill_metric
        self.unit_of_measurement = unit_of_measurement
        self.level1 = level1
        self.level2 = level2
        self.level3 = level3
        self.level4 = level4
        self.level5 = level5

class skillsdetail(db.model):
    __tablename__ = 'skillsdetail'
    skillid = db.Column(db.Integer, primary_key=True)
    skillname = db.Column(db.String(50))
    verb = db.Column(db.String(50))
    metric = db.Column(db.String(50))
    picture = db.Column(db.Text)
    description = db.Column(db.Text)

    def __init__(self, skillname, verb, metric, picture, description):
        self.skillname = skillname
        self.verb = verb
        self.metric = metric
        self.picture = picture
        self.description = description
'''

def init_app():

    with app.app_context():
        # Import parts of our core Flask app
        from . import routes

        # Import Dash application
        from .plotlydash.dashboard import create_dashboard
        app = create_dashboard(app)

        return app

def render_page(html_page, action):
    if action == "Bench Press":
        skillname = 'the bench press'
        skillverb = 'press'
        skillmetric = 'lbs'
        picture = 'https://cdn2.picryl.com/photo/2011/06/04/hiroko-yanai-bench-presses-99-pounds-during-the-2011-36d1e9-1600.jpg'
        description = 'A bench press is a compound a bodybuilding and weightlifting exercise in which a lifter lies on a bench with the feet on the floor and raises a weight with both arms.'
        return render_template(html_page, skillname=skillname, skillverb=skillverb, skillmetric=skillmetric, picture=picture, description=description)
    elif action == "Mile Run Time":
        skillname = 'mile run time'
        skillverb = 'run a mile'
        skillmetric = 'minutes'
        picture = "http://cdn.mos.cms.futurecdn.net/v44n2mBJgaRoCkkFGjDtRP.jpeg"
        description = 'Running is the activity of moving fast on foot, especially as a sport. The 1-mile run is a common measurement of aerobic fitness.'
        return render_template(html_page, skillname=skillname, skillverb=skillverb, skillmetric=skillmetric, picture=picture, description=description)       
    else:
        return render_template(html_page)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("home.html")

@app.route('/index/')
def index_page():
    return render_template("index.html")

@app.route('/mypage')
def my_page():
    return render_template("list.html")

@app.route('/enterInfo', methods=['GET', 'POST'])
def enter_info():

##Here, would be ideal to query the database to find which row "request.form['skillname']" corresponds to
	##then, if the method is 'POST' (which it will always be in the finished product) we just pull from the database to set all the variables

    if request.method == 'POST':
### This is where we would pull from the database to set all the HTML variables
        action = request.form['action']
        return render_page("enterInfo.html", action)
    else:
        #skillname = 'the bench press'
        #skillverb = 'press'
        #skillmetric = 'lbs'
        #picture = 'https://cdn2.picryl.com/photo/2011/06/04/hiroko-yanai-bench-presses-99-pounds-during-the-2011-36d1e9-1600.jpg'
        #description = 'A bench press is a compound a bodybuilding and weightlifting exercise in which a lifter lies on a bench with the feet on the floor and raises a weight with both arms.'
        return render_template("enterInfo.html"''', skillname=skillname, skillverb=skillverb, skillmetric=skillmetric, picture=picture, description=description''')

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    return render_template("login.html")

@app.route('/newcategory', methods=['GET', 'POST'])
def newCategory_page():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        return render_template("new_category.html", username=username, password=password)
    else:
        return render_template("new_category.html", username='', password='')

@app.route('/results/', methods=['GET', 'POST'])
def results_page():

##similar to the enterInfo page, pull from the database when we receive the post request to set the variables

    skill_name = "hot dog eating"
    count_responses = "1"
    calc_percentile = "100"
    top_perc = "0"
    bottom_perc = "99"
    
    if request.method == 'POST':
        score = request.form['score']
        return render_template("results.html", score=score, skill_name=skill_name, count_responses=count_responses, calc_percentile = calc_percentile, top_perc=top_perc, bottom_perc = bottom_perc)
    else:
        return render_template("results.html", score='No info entered', skill_name=skill_name, count_responses=count_responses, calc_percentile = calc_percentile, top_perc=top_perc, bottom_perc = bottom_perc)


