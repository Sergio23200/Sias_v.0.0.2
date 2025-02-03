from config.db import Base
from sqlalchemy import Column, Integer, String, Date, Boolean
from datetime import datetime


class Medications_model(Base):
    """
    este es el modelo de base de datos para la tabla de Medications_model, en el cual 
    se ven las columnas necesarias y el tipo de datos que se va autilizar, 
    tambien se daran cuenta cual es la llave primaria
    """

    __tablename__ = "Medications_stock"

    id = Column(Integer, primary_key=True)
    generic_name = Column(String, unique=True)
    dose = Column(Integer)
    price = Column(Integer)
    contraindications = Column(String)
    created_by = Column(Integer)
    aviable = Column(Boolean, default=True)
    Stocks = Column(Integer)
    created_date = Column(Date, default=datetime.utcnow)
