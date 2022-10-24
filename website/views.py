from datetime import date
from flask import Blueprint,render_template,request,flash,redirect,url_for
from flask_login import login_required,current_user
from website.models import Patients,Doctors,Appointments
from . import db

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("index.html",user=current_user)

@views.route('/about')
def about():
    return render_template("tabs/about.html",user=current_user)

@views.route('/contact',methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phn = request.form.get('phone')
        address = request.form.get('address')
        problem = request.form.get('problem')
        date = request.form.get('date')
        time = request.form.get('time')
        appt = Appointments.query.filter_by(email=email).first()
        if appt:
            flash('Appointment already booked from this email!', category='error')
        elif len(name)<2:
            flash('Name must be greater than 2 characters', category='error')
        else:
            new_appt = Appointments(name=name,email=email,number=phn,address=address,problem=problem,date=date,time=time)
            db.session.add(new_appt)
            db.session.commit()
            flash('Appointment booked successfully!', category='success')
            return redirect(url_for('views.home'))
    return render_template("tabs/contact.html",user=current_user)

@views.route('/services')
def services():
    return render_template("tabs/services.html",user=current_user)

@views.route('/doctors')
def doctors():
    return render_template("tabs/doctors.html",user=current_user)

@views.route('/patients')
@login_required
def patients():
    return render_template("tabs/patients.html",user=current_user)