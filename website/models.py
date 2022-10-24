from dataclasses import field
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Patients(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(150))
    lname = db.Column(db.String(150))
    number = db.Column(db.Integer)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))

class Doctors(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    field = db.Column(db.String(150))
    number = db.Column(db.Integer)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))

class Appointments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'))
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'))
    patient = db.relationship('Patients', backref=db.backref('appointments', lazy=True))
    doctor = db.relationship('Doctors', backref=db.backref('appointments', lazy=True))
