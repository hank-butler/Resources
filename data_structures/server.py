from sqlite3 import Connection as SQLiteConnection
from flask import Flask, request, jsonify
from sqlalchemy import event
from sqlalchemy.engine import Engine
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///sqlitedb.file'
app.config["SQL_TRACK_MODIFICATIONS"] = 0

# models for each table
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    address = db.Column(db.String(200))
    phone = db.Column(db.String(50))
    posts = db.relationship("BlogPost")
