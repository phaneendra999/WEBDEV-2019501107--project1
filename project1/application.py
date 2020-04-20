import os,sys,logging,time
from models import *
import datetime
from flask import escape, session


from flask import Flask, session,redirect,request,render_template,url_for
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

import hashlib

# from model import Users,db


app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
Session(app)
db.init_app(app)


# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))
sess = db()


# def main():
#     db.create_all()


# @app.route("/")
# def index():
#     return "Project 1: TODO"

@app.route("/register", methods = ["POST","GET"])   
def register():
    # db.create_all()
    if request.method == "POST":
 
        # result = request.form
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("psw")
        timestamp = datetime.datetime.now()
        new_users = Users(name = name,email = email,password = hashlib.md5(password.encode()).hexdigest(),timestamp=timestamp)
        
        try:
            sess.add(new_users)
            print(new_users)
            sess.commit()
            # name = name
            # print("commit completed")
            return render_template("result.html",name = name)
        except:

            text ="Account already exists!please try again with new account or login"
            return render_template("error.html",text = text)
    else:
        return render_template("register.html")            

       
        


@app.route("/admin", methods = ["GET"])
def users_info():
    # data = Users.query.all()
    data = db.query(Users)
    return render_template("users.html",data = data)     
@app.route("/")
def index():
    if request.method == "GET":
        if session.get("email") is not None:
            return render_template("home.html",text= session['email'])
        return redirect(url_for("register"))  



    #  Authentication
@app.route("/auth",methods=["POST"])    
def authentication():
    email = request.form['email']
    password = request.form['psw']
    pswd = hashlib.md5(password.encode()).hexdigest()
    data = db.query(Users).filter_by(email=email)
    if data[0].email == email and data[0].password == pswd:
        session["email"] = data[0].email
        # session["password"] = data[0].password
        return render_template("home.html",text = "welcome to Goodreads!!")
    return render_template("register.html",text = "email or password is incorrect")    

@app.route("/home")
def home():
    try:
        user = session['email']
        return render_template("home.html")     
    except:
        text = "you must first login to view the homepage"
        return render_template("register.html",text = text)
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")