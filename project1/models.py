from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = "Users"
    # id = db.Column(db.Serial,primary_key = True,nullable = False)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, primary_key=True)
    password = db.Column(db.String, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)


    def __init__(self,name,email,password,timestamp):
        self.name = name
        self.email = email
        self.password = password
        self.timestamp = timestamp

''' class for books'''
class Book(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer,primary_key = True)
    isbn = db.Column(db.String(100), unique = True,nullable = False)
    title = db.Column(db.String(100), unique = False,nullable = False)
    author = db.Column(db.String(128))
    year = db.Column(db.Integer,nullable=False)


    def __init__(self,isbn,title,author,year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year    

    # def __repr__(self):
    #     return self.title    