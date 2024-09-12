# importacion de librerias
from peewee import MySQLDatabase, BooleanField, AutoField, CharField, DateField, Model, IntegerField, TimeField
import datetime  # importacion para menjeo de fechas y hora

# Configuración de la base de datos
database = MySQLDatabase(
    'SIAS_sura',
    host='localhost',
    port=3306,
    user='root',
    password='Sergi@123'
)


class Affiliate(Model):
    id = AutoField()
    fullname = CharField(null=False)
    document_type = CharField(null=False)
    document_number = IntegerField(null=False, unique=True)
    birthdate = DateField(null=False)
    gender = CharField(null=False)
    email = CharField(index=True, unique=True, null=False)
    Address = CharField(null=False)
    Clinical_history = CharField(null=False)
    phone_number = IntegerField(null=False)  # Cambiado a CharField
    city = CharField(index=True, null=False)
    password = CharField(null=False)
    membership_type = CharField(null=False)
    created_date = DateField(default=datetime.date.today)

    class Meta:
        database = database
        db_table = 'Affiliate'


class Admin(Model):  # creación de tablas
    id = AutoField()  # llamado a llave primaria
    fullname = CharField(null=False)
    document_type = CharField(null=False)
    document_number = IntegerField(null=False)
    birthdate = DateField(null=False)
    email = CharField(index=True, unique=True, null=False)
    first_number = CharField(null=False)
    city = CharField(index=True, null=False)
    password = CharField(null=False)
    job_title = CharField(null=False)
    created_date = DateField(default=datetime.date.today)

    class Meta:
        database = database
        db_table = 'Admin'  # confirmacion de elemento


class medical_appointments(Model):  # Creación de tablas
    id = AutoField()  # llamado a llave primaria
    appointment_type = CharField(null=False)
    fullname_affiliate = CharField(null=False)
    document_number_affiliate = IntegerField(null=False)
    name_doctor = CharField(null=False)
    created_by = IntegerField()
    day = DateField()
    hospital_name = CharField(null=False)
    Clinical_history = CharField(null=False)
    create_date = DateField(default=datetime.date.today)
    hour = TimeField(null=False)

    class Meta:
        database = database  # confirmacion de elemento
        db_table = 'medical_appointments'


class Specialist(Model):
    id = AutoField()  # Llave primaria
    fullname = CharField(null=False)
    number_document = IntegerField(unique=True)
    email = CharField(index=True, unique=True, null=False)
    phone_number = IntegerField(null=False)
    specialty = CharField(null=False)
    create_date = DateField(default=datetime.date.today)
    created_by = IntegerField(null=False)  # Nombre correcto del campo

    class Meta:
        database = database  # Confirmación de la base de datos
        db_table = "Specialist"


class Hospital(Model):  # Creación de tabla
    id = AutoField()  # llamado a llave primaria
    fullname = CharField(null=False)
    city = CharField(null=False)
    Address = CharField(null=False)
    email = CharField(index=True, unique=True, null=False)
    phone_number = IntegerField(null=False)
    ambulance_dispo = IntegerField(null=False)
    ambulances_on_route = IntegerField()
    created_by = IntegerField()

    class Meta:
        database = database  # confirmacion de elemento
        db_table = "Hospital"


class Ips(Model):  # Creación de tabla
    id = AutoField()  # llamado a llave primaria
    fullname = CharField(null=False)
    city = CharField(null=False)
    Address = CharField(null=False)
    email = CharField(index=True, unique=True, null=False)
    phone_number = IntegerField(null=False)
    created_by = IntegerField()

    class Meta:
        database = database  # confirmacion de elemento
        db_table = "Health_Centers"


class Medications(Model):  # Creación de tabla
    id = AutoField()  # llamado a llave primaria
    generic_name = CharField(null=False)
    dose = IntegerField(null=False)
    price = IntegerField(null=False)
    contraindications = CharField(null=False)
    created_by = IntegerField()
    aviable = BooleanField(default=True)
    Stocks = IntegerField(null=False)

    class Meta:
        database = database  # confirmacion de elemento
        db_table = "Medications"


if __name__ == "__main__":
    database.connect()  # Conectar a la base de datos
    database.create_tables([Affiliate, Admin, medical_appointments,
                           Specialist, Hospital, Ips, Medications])
    database.close()  # Cerrar la conexión a la base de datos
