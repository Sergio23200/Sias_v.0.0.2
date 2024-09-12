from config.db import database
from peewee import AutoField, CharField, DateField, Model, IntegerField
import datetime


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
