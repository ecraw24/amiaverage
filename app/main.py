HEROKU_APP_NAME = "amiaverage"
TABLE_NAME = "skillsinfo"

from pickle import NONE
from unicodedata import category
from flask import Flask, render_template, current_app, request, url_for
from flask_sqlalchemy import SQLAlchemy
import matplotlib.pyplot as plt
from io import BytesIO
import base64


#This sets up our flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://nvalcjgkjirosy:a1d078c1ef28b3ccb5d5f9ff4583e42243fbd419766d05dacafd70e3dbd79d62@ec2-3-217-251-77.compute-1.amazonaws.com:5432/d4ecfjhp2gbtco"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


#These commands set up our connection to the database
#conn_info = subprocess.run(["heroku", "config:get", "DATABASE_URL", "-a", HEROKU_APP_NAME], stdout = subprocess.PIPE)
#connuri = conn_info.stdout.decode('utf-8').strip()
#conn = psycopg2.connect(connuri)
#cursor = conn.cursor()

#this creates our database object
db = SQLAlchemy(app)

#class for the 'skillsinfo' table
    #In this way, the table is an object, and we can get the rows through queries
        # row = killsinfo.query.filter_by(skill_name='SKILLNAME').first()
            #returns the row where the column for skill_name = 'SKILLNAME'
        # The values/attributes for each column can then be obtained via row.attribute
class skillsinfo(db.Model):
    __tablename__  = 'skillsinfo'
    id = db.Column(db.Integer, primary_key=True)
    skill_name = db.Column(db.String(50))
    skill_verb = db.Column(db.String(50))
    skill_metric = db.Column(db.String(50))
    unit_of_measurement = db.Column(db.String(50))
    picture = db.Column(db.Text)
    descrip = db.Column(db.Text)
    level1 = db.Column(db.Integer)
    level2 = db.Column(db.Integer)
    level3 = db.Column(db.Integer)
    level4 = db.Column(db.Integer)
    level5 = db.Column(db.Integer)

    def __init__(self, skill_name, skill_verb, skill_metric, unit_of_measurement, picture, descrip, level1, level2, level3, level4, level5):
        self.skill_name = skill_name
        self.skill_verb = skill_verb
        self.skill_metric = skill_metric
        self.unit_of_measurement = unit_of_measurement
        self.picture = picture
        self.descrip = descrip
        self.level1 = level1
        self.level2 = level2
        self.level3 = level3
        self.level4 = level4
        self.level5 = level5

#class for the suggestions tables
class suggestions(db.Model):
    __tablename__ = 'suggestions'
    skill_name = db.Column(db.String(50), primary_key=True)
    skill_verb = db.Column(db.String(50))
    skill_metric = db.Column(db.String(50))
    unit_of_measurement = db.Column(db.String(50))
    descrip = db.Column(db.Text)

    def __init__(self, skill_name, skill_verb, skill_metric, unit_of_measurement, descrip):
        self.skill_name = skill_name
        self.skill_verb = skill_verb
        self.skill_metric = skill_metric
        self.unit_of_measurement = unit_of_measurement
        self.descrip = descrip

#class for the 'skillsdetail' table
class skillsdetail(db.Model):
    __tablename__ = 'skillsdetail'
    skillid = db.Column(db.Integer, primary_key=True)
    skill_name = db.Column(db.String(50))
    skill_verb = db.Column(db.String(50))
    skill_metric = db.Column(db.String(50))
    picture = db.Column(db.Text)
    descrip = db.Column(db.Text)

    def __init__(self, skill_name, skill_verb, skill_metric, picture, descrip):
        self.skill_name = skill_name
        self.verb = skill_verb
        self.metric = skill_metric
        self.picture = picture
        self.descrip = descrip


def init_app():

    with app.app_context():
        # Import parts of our core Flask app
        from . import routes

        # Import Dash application
        from .plotlydash.dashboard import create_dashboard
        app = create_dashboard(app)

        return app

# function that returns the render_template() function with proper parameters for the enterInfo
# page depending on what link was clicked on the home page (link is represented by the action
# parameter, and is just the skill/category)
    #this function queries the database
def render_enter_info_page(html_page, action):

    #this line retrieves the 'Bench Press' row from the skillsinfo table
    row = skillsinfo.query.filter_by(skill_name=action).first()

    #if query failed (i.e. if 'action' was not in the skillsinfo table):
    if (row == NONE):
        return render_template(html_page)
    #if query was successful:
    else:
        #below, we set all the variables using the queries we obtained above
        skillname = row.skill_name #'the bench press'
        skillverb = row.skill_verb #'press'
        skillmetric = row.skill_metric #'lbs'
        picture = row.picture #'https://cdn2.picryl.com/photo/2011/06/04/hiroko-yanai-bench-presses-99-pounds-during-the-2011-36d1e9-1600.jpg'
        descrip = row.descrip #'A bench press is a compound a bodybuilding and weightlifting exercise in which a lifter lies on a bench with the feet on the floor and raises a weight with both arms.'
        return render_template(html_page, skillname=skillname, skillverb=skillverb, skillmetric=skillmetric, picture=picture, description=descrip)
        #"http://cdn.mos.cms.futurecdn.net/v44n2mBJgaRoCkkFGjDtRP.jpeg"
    
########
# Section for page routes 
########

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
        action = request.form['action'] #This is the activity we clicked on the home page
        return render_enter_info_page("enterInfo.html", action)
    else:
        #right now this renders the enter info page without any specifics
            #would be better if this would just take us back to the home page
                #i.e. call index(), but with an error message present
        return render_template("enterInfo.html")

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    return render_template("login.html")

@app.route('/newcategory', methods=['GET', 'POST'])
def newCategory_page():
    #check in post request for if the suggestion was valid
        #perhaps call this from success_page()
            #use a variable as a parameter???
    if request.method == 'POST':
        return render_template("new_category.html")
    else:
        return render_template("new_category.html")

@app.route('/submit', methods=['GET', 'POST'])
def submit_page():
    if request.method == 'POST':
        #below are the request form variables from the new_category page
        categoryName = request.form['categoryName'].lower()
        verb = request.form['verb']
        metric = request.form['metric']
        desc = request.form['desc']
        unit = request.form['unit_of_measurement']


        #if the category has already been suggested
        if db.session.query(suggestions).filter_by(skill_name=categoryName).first() != None:
            return render_template("new_category.html", message="Suggestion has already been made. Please enter another one.")
        #if there are no issues, render the success page and add to the database
        data = suggestions(categoryName, verb, metric, unit, desc)
        db.session.add(data)
        db.session.commit()
        return render_template("success.html")
    else:
        return "ERROR: INVALID METHOD OF REACHING PAGE"

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
        skillname = request.form['skill_name']
        return render_results_page("results.html", score, skillname)
    else:
        return render_template("results.html", score='No info entered', skill_name=skill_name, count_responses=count_responses, calc_percentile = calc_percentile, top_perc=top_perc, bottom_perc = bottom_perc)


#########
#END Section for page routes
#########


#function for rendering the results page
def render_results_page(html_page, score, action):
    #query the skillsinfo table for the row with skill_name = action
    row = skillsinfo.query.filter_by(skill_name=action).first()
    if row == NONE:
        return render_template("results.html", score='No info entered')
    else:
        #Mediocre...
        level1 = int(row.level1)
        #below average
        level2 = int(row.level2) 
        #slightly below average
        level3 = int(row.level3)
        #slightly above average
        level4 = int(row.level4)
        #above average
        level5 = int(row.level5)
        #Superb!
        skillname = row.skill_name
        (percentile, level) = get_percentile(int(score), [level1, level2, level3, level4, level5])
        plot_url = plot_graph([level1, level2, level3, level4, level5])
        return render_template(html_page, score=score, level=level, top_perc=100-percentile, skill_name=skillname, calc_percentile=percentile, level1=level1, level2=level2, level3=level3, level4=level4, level5=level5, plot_url=plot_url)

#returns the percentile and corresponding string that the score achieved for a skill
def get_percentile(score, list):
    place = 0
    #loop sets 'place' to 0 if below level1, 1 if between 1 and 2, ..., 5 if greater than level5
    strings = ["Mediocre...", "Below Average", "Slightly Below Average", "Slightly Above Average", "Above Average",  "Superb!"]
    for i, elt in enumerate(list):
        if score > elt:
            place = i + 1
        else:
            break
    #now, we calculate a rough percentage
        #this is very poor, just serving as a temporary placeholder
    if place == 5:
        return (100, strings[place])
    if place == 0:
        return (0, strings[place])
    prev_lvl = list[place-1]
    next_lvl = list[place]
    return ((place * 20) + (score // (next_lvl - prev_lvl)), strings[place])

def plot_graph(level_list):
    img = BytesIO()

    # set up the figure
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xlim(0,10)
    ax.set_ylim(0,10)

    # draw lines
    x1 = 1
    x2=3
    x3=5
    x4=7
    x5 = 9

    y = 5
    height = 1

    plt.hlines(y, x1-1, x5+1)
    plt.vlines(x1, y - height / 2., y + height / 2.)
    plt.vlines(x2, y - height / 2., y + height / 2.)
    plt.vlines(x3, y - height / 2., y + height / 2.)
    plt.vlines(x4, y - height / 2., y + height / 2.)
    plt.vlines(x5, y - height / 2., y + height / 2.)

    # draw a point on the line
    px = 4
    plt.plot(px,y, 'ro', ms = 15, mfc = 'r')

    # add an arrow
    plt.annotate('Your score', (px,y), xytext = (px - 1, y + 1), 
                arrowprops=dict(facecolor='black', shrink=0.1), 
                horizontalalignment='right')

    # add numbers
    plt.text(x1-0.1, y-1, '1', verticalalignment='center_baseline')
    plt.text(x2-0.1, y-1, '3', verticalalignment='center_baseline')
    plt.text(x3-0.1, y-1, '5', verticalalignment='center_baseline')
    plt.text(x4-0.1, y-1, '7', verticalalignment='center_baseline')
    plt.text(x5-0.1, y-1, '9', verticalalignment='center_baseline')

    plt.axis('off')

    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf-8')
        
    return plot_url
    
