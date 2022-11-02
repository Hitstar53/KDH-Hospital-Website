from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'kdh5253'
    #old db - sqLite
    #app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    #new db - mysql localhost
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://sqluser:password@localhost/hospital'
    #new db - free awd
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:hospital123@hospital.c36zbkr1bobf.ap-south-1.rds.amazonaws.com:3306/hospital'
    #new db - freesqldatabase
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://sql12533559:bum3pMdUv1@sql12.freesqldatabase.com:3306/sql12533559'
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://Hitstar53:hospital123@Hitstar53.mysql.pythonanywhere-services.com:3306/Hitstar53$hospital'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import Patients,Doctors,Appointments
    create_database(app)
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return Patients.query.get(int(id))
    return app

def create_database(app):
    with app.app_context():
        db.create_all()
    print('Created Database!')