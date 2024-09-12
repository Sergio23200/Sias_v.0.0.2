from config.db import database
from peewee import MySQLDatabase, BooleanField, AutoField, CharField, DateField, Model, IntegerField, TimeField


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
