from flask import Flask, render_template
#import os
#import psycopg2

#DATABASE_URL = os.environ['DATABASE_URL']

#conn = psycopg2.connect(DATABASE_URL, sslmode='require')

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
    return render_template("enterInfo.html")
