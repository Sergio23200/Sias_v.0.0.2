from config.db import Base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime


class Specialist_model(Base):
    """
    este es el modelo de base de datos para la tabla de Specialist_model, en el cual 
    se ven las columnas necesarias y el tipo de datos que se va autilizar, 
    tambien se daran cuenta cual es la llave primaria
    """
    __tablename__ = "Specialist"
    id = Column(Integer, primary_key=True,  autoincrement=True)
    fullname = Column(String)
    number_document = Column(Integer, unique=True)
    email = Column(String, unique=True)
    phone_number = Column(String, unique=True)
    specialty = Column(String)
    created_date = Column(Date, default=datetime.utcnow)
    created_by = Column(Integer)
