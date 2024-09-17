from config.db import Base
from sqlalchemy import Column, Integer, String, Date, Time
from datetime import datetime


class Medical_appointments_model(Base):
    __tablename__ = "Medical_appointments"
    id = Column(Integer, primary_key=True)
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
