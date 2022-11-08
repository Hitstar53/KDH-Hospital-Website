from flask import Blueprint,render_template,request,flash,redirect,url_for,jsonify
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_required,current_user
from website.models import Patients,Doctors,Appointments,Payments
from . import db
from .auth import create_admin
import json

views = Blueprint('views', __name__)

@views.route('/')
def home():
    create_admin()
    return render_template("index.html",user=current_user)

@views.route('/admin',methods=['GET', 'POST'])
@login_required
def admin():
    return render_template("tabs/admin.html",user=current_user,patients=Patients.query.all())

@views.route('/admindoctors',methods=['GET', 'POST'])
@login_required
def admindoctors():
    if request.method == 'POST':
        formid = request.args.get('formid', 1, type=int)
        if formid == 1:
            name = request.form.get('name')
            age = request.form.get('age')
            number = request.form.get('number')
            email = request.form.get('email')
            field = request.form.get('field')
            doctor = Doctors(name=name,age=age,number=number,email=email,field=field)
            db.session.add(doctor)
            db.session.commit()
            flash('Doctor Added Successfully',category='success')
        if formid == 2:
            name = request.form.get('delname')
            email = request.form.get('delemail')
            doctor = Doctors.query.filter_by(email=email).first()
            if doctor:
                db.session.delete(doctor)
                db.session.commit()
                flash('Doctor Deleted Successfully',category='success')
            else:
                flash('No Doctor Found',category='error')
        return redirect(url_for('views.admindoctors'))
    return render_template("tabs/ad_doctors.html",user=current_user,doctors=Doctors.query.all())

@views.route('/adminpatients',methods=['GET', 'POST'])
@login_required
def adminpatients():
    if request.method == 'POST':
        formid = request.args.get('formid', 1, type=int)
        if formid == 1:
            fname = request.form.get('fname')
            lname = request.form.get('lname')
            phn = request.form.get('phone')
            email = request.form.get('email')
            password1 = request.form.get('password')
            password2 = request.form.get('confirm')
            patient = Patients.query.filter_by(email=email).first()
            if patient:
                flash('Email already exists.', category='error')
            elif password1 != password2:
                flash('Passwords do not match', category='error')
            elif len(password1) < 8:
                flash('Password must be at least 8 characters', category='error')
            else:
                patient = Patients(fname=fname, lname=lname, number=phn, email=email, password=generate_password_hash(password1, method='sha256'))
                db.session.add(patient)
                db.session.commit()
                flash('Patient Added Successfully',category='success')
        if formid == 2:
            fname = request.form.get('fname')
            lname = request.form.get('lname')
            email = request.form.get('delemail')
            patient = Patients.query.filter_by(email=email).first()
            if patient:
                db.session.delete(patient)
                db.session.commit()
                flash('Patient Deleted Successfully',category='success')
            else:
                flash('No Patient Found',category='error')
        return redirect(url_for('views.adminpatients'))
    return render_template("tabs/ad-patients.html",user=current_user,patients=Patients.query.all())

@views.route('/adminappointments',methods=['GET', 'POST'])
@login_required
def adminappointments():
    if request.method == 'POST':
        formid = request.args.get('formid', 1, type=int)
        if formid == 1:
            name = request.form.get('name')
            email = request.form.get('email')
            phn = request.form.get('phone')
            address = request.form.get('address')
            problem = request.form.get('problem')
            date = request.form.get('date')
            time = request.form.get('time')
            new_appt = Appointments(name=name,email=email,number=phn,address=address,problem=problem,date=date,time=time)
            db.session.add(new_appt)
            db.session.commit()
            flash('Appointment Added Successfully',category='success')
        if formid == 2:
            name = request.form.get('delname')
            email = request.form.get('delemail')
            appointment = Appointments.query.filter_by(email=email).first()
            if appointment:
                db.session.delete(appointment)
                db.session.commit()
                flash('Appointment Deleted Successfully',category='success')
            else:
                flash('No Appointment Found',category='error')
        return redirect(url_for('views.adminappointments'))
    return render_template("tabs/ad-appointments.html",user=current_user,appointments=Appointments.query.all())

@views.route('/adminanalytics')
@login_required
def adminanalytics():
    return render_template("tabs/ad-analytics.html",user=current_user)

@views.route('/admin-payments')
@login_required
def admin_payments():
    return render_template("tabs/ad-transactions.html",user=current_user,payments=Payments.query.all())

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
        #appt = Appointments.query.filter_by(email=email).first()
        #if appt:
        #    flash('Appointment already booked from this email!', category='error')
        if len(name)<=4:
            flash('Name must be greater than 4 characters', category='error')
        else:
            new_appt = Appointments(name=name,email=email,number=phn,address=address,problem=problem,date=date,time=time)
            db.session.add(new_appt)
            db.session.commit()
            flash('Appointment booked successfully!', category='success')
            return redirect(url_for('views.contact'))
    return render_template("tabs/contact.html",user=current_user)

@views.route('/services')
def services():
    return render_template("tabs/services.html",user=current_user)

@views.route('/doctors')
def doctors():
    return render_template("tabs/doctors.html",user=current_user,doctors=Doctors.query.all())

@views.route('/patients')
@login_required
def patients():
    return render_template("tabs/patients.html",user=current_user,patients=Patients.query.all())

@views.route('/appointments',methods=['GET', 'POST'])
@login_required
def appointments():
    return render_template("tabs/appointments.html",user=current_user,appointments=Appointments.query.all())

@views.route('/payments',methods=['GET','POST'])
@login_required
def payments():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        address = request.form.get('address')+','+request.form.get('city')+','+request.form.get('zipcode')
        amt = 690
        pstatus = 'success'
        new_payment = Payments(name=name,email=email,address=address,amount=amt,payment_status=pstatus)
        db.session.add(new_payment)
        db.session.commit()
        flash('Payment successful!', category='success')
    return render_template("tabs/payments.html",user=current_user,payments=Payments.query.all())

@views.route('/cancelAppointment',methods=['POST'])
def cancelAppointment():
    data = json.loads(request.data)
    apptId = data['appointmentId']
    appt = Appointments.query.get(apptId)
    if appt:
        db.session.delete(appt)
        db.session.commit()
    return jsonify({})