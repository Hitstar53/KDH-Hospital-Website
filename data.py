#method 1:
from werkzeug.security import generate_password_hash,check_password_hash
import sqlite3

conn = sqlite3.connect('instance/database.db')
cursor = conn.cursor()

#sql = f"INSERT INTO doctors VALUES(1,'John Doe',35,1234567890,'johndoe@gmail.com','cardiology')"
#cursor.execute(sql)
#conn.commit()

sql = f"INSERT INTO doctors VALUES(2,'John2 Doe',35,1234567890,'john2doe@gmail.com','neurology')"
cursor.execute(sql)
conn.commit()

sql = f"INSERT INTO doctors VALUES(3,'John3 Doe',35,1234567890,'john3doe@gmail.com','dermatology')"
cursor.execute(sql)
conn.commit()


#method 2:
'''from werkzeug.security import generate_password_hash,check_password_hash
from . import db
from .models import Patients,Doctors,Appointments

new_patient = Patients(fname='John',lname='Doe',number=1234567890,email='johndoe@gmail.com',password=generate_password_hash('123456789', method='sha256'))
db.session.add(new_patient)
db.session.commit()'''


