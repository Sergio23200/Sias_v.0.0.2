from config.db import Base
from datetime import datetime
from sqlalchemy import Column, Integer, String, Date


class Admin_model(Base):
    """
    este es el modelo de base de datos para la tabla de admin, en el cual 
    se ven las columnas necesarias y el tipo de datos que se va autilizar, 
    tambien se daran cuenta cual es la llave primaria
    """
    __tablename__ = "Admin"

    id = Column(Integer, autoincrement=True, primary_key=True)
    fullname = Column(String)
    document_type = Column(String)
    document_number = Column(Integer, unique=True)
    birthdate = Column(Date)
    email = Column(String, unique=True)
    first_number = Column(String)
    city = Column(String)
    password = Column(String)
    job_title = Column(String)
    created_date = Column(Date, default=datetime.utcnow)
