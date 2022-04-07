from flask import Flask, render_template
#import psycopg2

#conn = psycopg2.connect(dbname="d4ecfjhp2gbtco", user="nvalcjgkjirosy", password="a1d078c1ef28b3ccb5d5f9ff4583e42243fbd419766d05dacafd70e3dbd79d62", host="ec2-3-217-251-77.compute-1.amazonaws.com", sslmode="require")
#curs=conn.cursor()

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
    #skillname = curs.execute('SELECT skillname FROM skillsdetail WHERE skillid=3;').fetchall()
    #curs.close()
    #conn.close()
    skillname = 'example skill'
    return render_template("enterInfo.html", skillname=skillname)

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
