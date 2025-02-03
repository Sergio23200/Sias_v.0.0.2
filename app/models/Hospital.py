from config.db import Base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime


class Hospital_model(Base):
    """
    este es el modelo de base de datos para la tabla de Hospital_model, en el cual 
    se ven las columnas necesarias y el tipo de datos que se va autilizar, 
    tambien se daran cuenta cual es la llave primaria
    """
    __tablename__ = "Hospital"

    id = Column(Integer, primary_key=True, unique=True)
    name_hospital = Column(String)
    city = Column(String)
    Address = Column(String, unique=True)
    email = Column(String, unique=True)
    phone_number = Column(String, unique=True)
    ambulance_dispo = Column(Integer)
    ambulances_on_route = Column(Integer)
    create_by = Column(Integer)
    created_date = Column(Date, default=datetime.utcnow)
