from config.db import database
from peewee import AutoField, CharField, DateField, Model, IntegerField


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
