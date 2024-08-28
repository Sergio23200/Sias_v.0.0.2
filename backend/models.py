from peewee import MySQLDatabase, AutoField, CharField, DateField, Model, IntegerField #importacion de librerias 
import bcrypt
import datetime # importacion para menjeo de fechas y hora

# Configuración de la base de datos
database = MySQLDatabase(
    'SIAS_sura',
    host='localhost',  
    port=3306,
    user='root',
    password='Sergi@123'
)

class Affiliate(Model): # creacion de tablas
    id = AutoField() # llamado a llave primaria
    fullname = CharField(null=False)
    document_type = CharField(null=False)
    document_number = IntegerField(null=False, unique=True)
    birthdate = DateField(null=False)
    gender = CharField (null=False)
    email = CharField(index=True, unique=True, null=False)
    Address = CharField(null=False)
    phone_number = IntegerField(null=False)
    city = CharField(index=True, null=False)
    password = CharField(null=False)
    membership_type = CharField(null=False)
    created_date = DateField(default=datetime.date.today)
    
    class Meta:
        database = database
        db_table = 'Affiliate' #confirmacion de elemento 

class Admin(Model): # creación de tablas 
    id = AutoField() # llamado a llave primaria
    fullname = CharField(null=False)
    document_type = CharField(null=False)
    document_number = IntegerField(null=False)
    birthdate = DateField(null=False)
    email = CharField(index=True, unique=True, null=False)
    first_number = CharField(null=False)
    second_number = IntegerField()
    city = CharField(index=True, null=False)
    password = CharField(null=False)
    job_title = CharField(null=False)
    created_date = DateField(default=datetime.date.today)
    
    class Meta:
        database = database
        db_table = 'Admin' #confirmacion de elemento 

class Database(Model):#Creación de tablas
    id = AutoField() # llamado a llave primaria
    appointment_type = CharField (null=False)
    specialist = CharField (null=False)
    time_date = CharField (null=False)
    hospital_name = CharField (null=False)
    clinic_name = CharField (null=False)
    medications = CharField (null=False)
    Clinical_history = CharField (null=False)
    create_date = DateField(default=datetime.date.today)
    hour = IntegerField(null=False)
    
    class Meta:
        database = database #confirmacion de elemento 
        db_table = 'database'

class Specialist(Model):#Creación de tablas
     id = AutoField() # llamado a llave primaria
     fullname = CharField()
     number_document = IntegerField(unique=True)
     email = CharField(index=True, unique=True, null=False)
     phone_number = IntegerField(null=False)
     specialty = CharField(null=False)
     create_date = DateField(default=datetime.date.today)
     hour = IntegerField(null=False)

     class Meta:
          database = database #confirmacion de elemento
          db_table = "Specialist"

class Hospital(Model): #Creación de tabla
     id = AutoField() # llamado a llave primaria
     fullname = CharField(null=False)
     city_id = CharField(null=False)
     Address = CharField(null=False)
     specialty = CharField(null=False)
     email = CharField(index=True, unique=True, null=False)
     phone_number = IntegerField(null=False)
     ambulance = IntegerField(null=False)
     

     class Meta: 
          database = database #confirmacion de elemento
          db_table = "Hospital" 


class Health_Centers(Model): #Creación de tabla
     id = AutoField() # llamado a llave primaria
     fullname = CharField(null=False)
     city_id = CharField(null=False)
     Address = CharField(null=False)
     specialty = CharField(null=False)
     email = CharField(index=True, unique=True, null=False)
     phone_number = IntegerField(null=False)
     ambulance = IntegerField(null=False)
     

     class Meta: 
          database = database #confirmacion de elemento
          db_table = "Health_Centers"


class Medications(Model): #Creación de tabla
     id = AutoField() # llamado a llave primaria
     generic_name = CharField(null=False)
     dose = CharField(null=False)
     price = CharField(null=False)
     contraindications = CharField(null=False)
              

     class Meta: 
          database = database #confirmacion de elemento
          db_table ="Medications"
if __name__ == "__main__":
    database.connect()  # Conectar a la base de datos
    database.create_tables([Affiliate, Admin, Database, Specialist, Hospital, Health_Centers, Medications])
    database.close()  # Cerrar la conexión a la base de datos