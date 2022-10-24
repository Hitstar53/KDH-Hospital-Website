from flask import Blueprint,render_template
from flask_login import login_required,current_user

from website.models import Patients,Doctors,Appointments

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("index.html",user=current_user)

@views.route('/about')
def about():
    return render_template("tabs/about.html")

@views.route('/contact')
def contact():
    return render_template("tabs/contact.html")

@views.route('/services')
def services():
    return render_template("tabs/services.html")

@views.route('/doctors')
def doctors():
    return render_template("tabs/doctors.html")

@views.route('/patients')
@login_required
def patients():
    return render_template("tabs/patients.html")