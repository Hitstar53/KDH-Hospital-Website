#method 1:
#from werkzeug.security import generate_password_hash,check_password_hash
import sqlite3

conn = sqlite3.connect('instance/database.db')
cursor = conn.cursor()

sql = "INSERT INTO doctors VALUES(1,'John Doe',25,9898785357,'johndoe@gmail.com','cardiology')"
cursor.execute(sql)
conn.commit()

sql = "INSERT INTO doctors VALUES(2,'Thomas Shelby',45,7896545665,'thomasshelby@gmail.com','neurology')"
cursor.execute(sql)
conn.commit()

sql = "INSERT INTO doctors VALUES(3,'Michael Gray',20,8999876545,'michaelgray@gmail.com','dermatology')"
cursor.execute(sql)
conn.commit()

sql = "INSERT INTO doctors VALUES(4,'Ada Thorne',28,98786545687,'adathorne@gmail.com','Opthalmology')"
cursor.execute(sql)
conn.commit()

sql = "INSERT INTO doctors VALUES(5,'Arthur Shelby',50,9999988875,'arthurshelby@gmail.com','Dermatolgy')"
cursor.execute(sql)
conn.commit()

sql = "INSERT INTO doctors VALUES(6,'Charlie Hourse',55,9887889876,'charliehorses@gmail.com','Pathology')"
cursor.execute(sql)
conn.commit()

sql = "INSERT INTO doctors VALUES(7,'Billy Kimber',44,9877896540,'billykimber@gmail.com','Orthopedics')"
cursor.execute(sql)
conn.commit()

sql = "INSERT INTO doctors VALUES(8,'Alfie Solomon',60,8798797895,'alfiesolomons@gmail.com','Surgery')"
cursor.execute(sql)
conn.commit()

sql = "INSERT INTO doctors VALUES(9,'Polly Blackmagic',65,9788856786,'pollyblackmagic@gmail.com','Radiology')"
cursor.execute(sql)
conn.commit()

sql = "INSERT INTO doctors VALUES(10,'Mathew Modine',35,1234567890,'mathewmodine@gmail.com','Dentistry')"
cursor.execute(sql)
conn.commit()

sql = "INSERT INTO doctors VALUES(11,'Grace Locke',25,7777778889,'gracelocke@gmail.com','cardiology')"
cursor.execute(sql)
conn.commit()

sql = "INSERT INTO doctors VALUES(12,'Lucas Sinclair',25,7777778889,'lucassinclair@gmail.com','cardiology')"
cursor.execute(sql)
conn.commit()

sql = "INSERT INTO doctors VALUES(13,'Antonio Zuckerberg',25,7777778889,'antonioberg@gmail.com','cardiology')"
cursor.execute(sql)
conn.commit()

#method 2:
'''from werkzeug.security import generate_password_hash,check_password_hash
from . import db
from .models import Patients,Doctors,Appointments

new_patient = Patients(fname='John',lname='Doe',number=1234567890,email='johndoe@gmail.com',password=generate_password_hash('123456789', method='sha256'))
db.session.add(new_patient)
db.session.commit()'''


