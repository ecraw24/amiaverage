from flask import Flask, render_template, current_app, request, url_for

app = Flask(__name__)

def init_app():

    with app.app_context():
        # Import parts of our core Flask app
        from . import routes

        # Import Dash application
        from .plotlydash.dashboard import create_dashboard
        app = create_dashboard(app)

        return app

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
        skillname = 'the bench press'
        skillverb = 'press'
        skillmetric = 'lbs'
        picture = 'https://cdn2.picryl.com/photo/2011/06/04/hiroko-yanai-bench-presses-99-pounds-during-the-2011-36d1e9-1600.jpg'
        description = 'A bench press is a compound a bodybuilding and weightlifting exercise in which a lifter lies on a bench with the feet on the floor and raises a weight with both arms.'
    #if con is not None:
        #con.close()
        #print('Database connection closed.')
        return render_template("enterInfo.html", skillname=skillname, skillverb=skillverb, skillmetric=skillmetric, picture=picture, description=description)
    else:
        skillname = 'the bench press'
        skillverb = 'press'
        skillmetric = 'lbs'
        picture = 'https://cdn2.picryl.com/photo/2011/06/04/hiroko-yanai-bench-presses-99-pounds-during-the-2011-36d1e9-1600.jpg'
        description = 'A bench press is a compound a bodybuilding and weightlifting exercise in which a lifter lies on a bench with the feet on the floor and raises a weight with both arms.'
    #if con is not None:
        #con.close()
        #print('Database connection closed.')
        return render_template("enterInfo.html", skillname=skillname, skillverb=skillverb, skillmetric=skillmetric, picture=picture, description=description)

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


