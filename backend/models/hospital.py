from config.db import Base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime


class Hospital_model(Base):
    __tablename__ = "Hospital"

    id = Column(Integer, primary_key=True)
    name_hospital = Column(String)
    city = Column(String)
    Address = Column(String)
    email = Column(String)
    phone_number = Column(String)
    ambulance_dispo = Column(Integer)
    ambulances_on_route = Column(Integer)
    create_by = Column(Integer)
    created_date = Column(Date, default=datetime.utcnow)
