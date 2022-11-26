from dataclasses import field
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from sqlalchemy.dialects import mysql

class Patients(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(150))
    lname = db.Column(db.String(150))
    number = db.Column(mysql.BIGINT)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))

class Doctors(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    age = db.Column(db.Integer)
    number = db.Column(mysql.BIGINT)
    email = db.Column(db.String(150), unique=True)
    field = db.Column(db.String(150))

class Appointments(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    email = db.Column(db.String(150))
    number = db.Column(db.BIGINT)
    address = db.Column(db.String(150))
    problem = db.Column(db.String(150))
    doctor = db.Column(db.String(150))
    date = db.Column(db.String(150))
    time = db.Column(db.String(150))

class Payments(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    email = db.Column(db.String(150))
    address = db.Column(db.String(150))
    amount = db.Column(db.Integer)
    payment_status = db.Column(db.String(150))
