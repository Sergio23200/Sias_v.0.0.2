from config.db import database
from peewee import AutoField, CharField, BooleanField, Model, IntegerField
import datetime


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
