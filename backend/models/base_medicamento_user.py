from config.db import Base
from sqlalchemy import Column, Integer, String, Date, Boolean
from datetime import datetime


class base_medications_model(Base):
    """
    este es el modelo de base de datos para la tabla de base_medications_model, en el cual 
    se ven las columnas necesarias y el tipo de datos que se va autilizar, 
    tambien se daran cuenta cual es la llave primaria
    """
    __tablename__ = "Medications_base_user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    generic_name = Column(String)
    affiliate = Column(String)
    Stocks = Column(Integer)
