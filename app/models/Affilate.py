from config.db import Base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime


class Affiliate_model(Base):
    __tablename__ = "Affiliate"
    """
    este es el modelo de base de datos para la tabla de affiliate, en el cual 
    se ven las columnas necesarias y el tipo de datos que se va autilizar, 
    tambien se daran cuenta cual es la llave primaria
    """

    id = Column(Integer, primary_key=True, autoincrement=True)
    fullname = Column(String)
    document_type = Column(String)
    document_number = Column(String, unique=True)
    birthdate = Column(Date)
    Address = Column(String)
    gender = Column(String)
    email = Column(String, unique=True)
    phone_number = Column(String)
    city = Column(String)
    password = Column(String)
    membership_type = Column(String)
    Clinical_history = Column(Integer)
    created_date = Column(Date, default=datetime.utcnow)
