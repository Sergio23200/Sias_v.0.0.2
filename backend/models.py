from peewee import MySQLDatabase, AutoField, CharField, DateField, Model, IntegerField #importacion de librerias 
import datetime # importacion para menjeo de fechas y hora

# Configuración de la base de datos
database = MySQLDatabase(
    'SIAS_sura',
    host='localhost',  
    port=3306,
    user='root',
    password='Sergi@123'
)

# charfield texto
# intergerfield numericos
#  datafield fechas
# AutoField

class affiliates(Model): # creacion de tablas
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
    membership_type = CharField(null=False)
    created_date = DateField(default=datetime.date.today)
    
    class Meta:
        database = database
        db_table = 'affiliates' #confirmacion de elemento 

class admin(Model): # creacion de tablas 
    id = AutoField()
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
        db_table = 'admin' #confirmacion de elemento 

class create_appointment(Model):#confirmacion de elemento 
    id = AutoField() 
    create_by = CharField(null=False, index=True)
    create_date = DateField(default=datetime.date.today)
    appointment_type = CharField(null=False)
    hour = IntegerField(null=False)
    
    class Meta:
        database = database #confirmacion de elemento 
        db_table = 'create_appointment'
class Person(Model):
     id = AutoField()
     fullname = CharField()
     number_document = IntegerField(inque = True)
if __name__ == '__main__':
        # Conectar a la base de datos
        database.connect()
