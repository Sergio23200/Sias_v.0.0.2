from config.db import database
from peewee import AutoField, CharField, DateField, Model, IntegerField
import datetime


class Specialist(Model):
    id = AutoField()  # Llave primaria
    fullname = CharField(null=False)
    number_document = IntegerField(unique=True)
    email = CharField(index=True, unique=True, null=False)
    phone_number = IntegerField(null=False)
    specialty = CharField(null=False)
    create_date = DateField(default=datetime.date.today)
    created_by = IntegerField(null=False)

    class Meta:
        database = database
        db_table = "Specialist"
