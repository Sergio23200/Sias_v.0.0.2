from config.db import Base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime


class Ips_model(Base):
    """
    este es el modelo de base de datos para la tabla de Ips_model, en el cual 
    se ven las columnas necesarias y el tipo de datos que se va autilizar, 
    tambien se daran cuenta cual es la llave primaria
    """
    __tablename__ = "Ips"

    id = Column(Integer, primary_key=True, unique=True)
    name_hospital = Column(String)
    city = Column(String)
    Address = Column(String, unique=True)
    email = Column(String, unique=True)
    create_by = Column(Integer)
    phone_number = Column(String, unique=True)
    create_by: int = Column(String)
    created_date = Column(Date, default=datetime.utcnow)
