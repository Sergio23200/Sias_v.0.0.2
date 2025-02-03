from config.db import Base
from sqlalchemy import Column, Integer, String, Date, Time
from datetime import datetime


class Medical_appointments_model(Base):
    """
    este es el modelo de base de datos para la tabla de Medical_appointments_model, en el cual 
    se ven las columnas necesarias y el tipo de datos que se va autilizar, 
    tambien se daran cuenta cual es la llave primaria
    """
    __tablename__ = "Medical_appointments"
    id = Column(Integer, primary_key=True, autoincrement=True)
    appointment_type = Column(String)
    fullname_affiliate = Column(String)
    document_number_affiliate = Column(Integer)
    name_doctor = Column(String)
    created_by = Column(String)
    day = Column(Date)
    hospital_name = Column(String)
    Clinical_history = Column(Integer)
    created_date = Column(Date, default=datetime.utcnow)
    hour = Column(Time)
