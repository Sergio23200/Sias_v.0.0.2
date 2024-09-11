from config.db import database
from peewee import AutoField, CharField, DateField, Model, IntegerField
import datetime


class Affiliate(Model):
    """

    """
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
