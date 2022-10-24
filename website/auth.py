from flask import Blueprint,render_template,request,flash,redirect,url_for
from flask_login import login_user,login_required,logout_user,current_user
from werkzeug.security import generate_password_hash,check_password_hash
from . import db
from .models import Patients,Doctors,Appointments

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = Patients.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')
    return render_template("tabs/login.html",user=current_user)

@auth.route('forgot-password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form.get('email')
        password1 = request.form.get('password')
        password2 = request.form.get('confirm')
        user = Patients.query.filter_by(email=email).first()
        if password1 != password2:
            flash('Passwords do not match', category='error')
        elif len(password1) < 8:
            flash('Password must be at least 8 characters', category='error')
        elif user:
            user.password = generate_password_hash(password1, method='sha256')
            db.session.commit()
            flash('Password has been reset', category='success')
            return redirect(url_for('auth.login'))
        else:
            flash('Email does not exist.', category='error')
    return render_template("tabs/forgot.html",user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully!', category='success')
    return redirect(url_for('auth.login'))

@auth.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        fname = request.form.get('fname')
        sname = request.form.get('sname')
        phn = request.form.get('phone')
        email = request.form.get('email')
        password1 = request.form.get('password')
        password2 = request.form.get('confirm')
        print(fname, sname, phn, email, password1, password2)
        user = Patients.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif password1 != password2:
            flash('Passwords do not match', category='error')
        elif len(password1) < 8:
            flash('Password must be at least 8 characters', category='error')
        #check if password has at least 1 letter and 1 number
        #elif not any(char.isdigit() for char in password1) or not any(char.isalpha() for char in password1):
        #    flash('Password must contain letters & numbers', category='error')
        else:
            new_user = Patients(fname=fname, lname=sname, number=phn, email=email, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))
    return render_template("tabs/signup.html",user=current_user)
