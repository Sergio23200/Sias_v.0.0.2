from config.db import Base
from sqlalchemy import Column, Integer, String, Date, Boolean
from datetime import datetime


class Medications_model(Base):
    __tablename__ = "Medications"

    id = Column(Integer, primary_key=True)
    generic_name = Column(String)
    dose = Column(Integer)
    price = Column(Integer)
    contraindications = Column(String)
    created_by = Column(Integer)
    aviable = Column(Boolean)
    Stocks = Column(Integer)
    created_date = Column(Date, default=datetime.utcnow)
