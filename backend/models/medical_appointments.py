from config.db import database
from peewee import AutoField, CharField, DateField, Model, IntegerField, TimeField
import datetime


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
