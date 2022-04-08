from flask import Flask, render_template
from dbconnect import enterInfo

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")

@app.route('/index/')
def index_page():
    return render_template("index.html")

@app.route('/mypage')
def my_page():
    return render_template("list.html")

@app.route('/enterInfo')
def enter_info():
    skillname = enterInfo()
    skillverb = 'press'
    skillmetric = 'lbs'
    picture = 'https://cdn2.picryl.com/photo/2011/06/04/hiroko-yanai-bench-presses-99-pounds-during-the-2011-36d1e9-1600.jpg'
    description = 'A bench press is a compound a bodybuilding and weightlifting exercise in which a lifter lies on a bench with the feet on the floor and raises a weight with both arms.'
    #if con is not None:
        #con.close()
        #print('Database connection closed.')
    return render_template("enterInfo.html", skillname=skillname, skillverb=skillverb, skillmetric=skillmetric, picture=picture, description=description)

@app.route('/login')
def login_page():
    return render_template("login.html")

@app.route('/newcategory')
def newCategory_page():
    return render_template("new_category.html")

@app.route('/results/')
def results_page():
    skill_name = "hot dog eating"
    count_responses = "1"
    calc_percentile = "100"
    top_perc = "0"
    bottom_perc = "99"

    return render_template("results.html", skill_name=skill_name, count_responses=count_responses,
    calc_percentile = calc_percentile, top_perc=top_perc, bottom_perc = bottom_perc)

#cur.close()
#con.close()
