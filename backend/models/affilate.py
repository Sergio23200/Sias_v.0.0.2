from config.db import Base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime


class Affiliate_model(Base):
    __tablename__ = "Affiliate"

    id = Column(Integer, primary_key=True)
    fullname = Column(String)
    document_type = Column(String)
    document_number = Column(String)
    birthdate = Column(Date)
    Address = Column(String)
    gender = Column(String)
    email = Column(String)
    phone_number = Column(String)
    city = Column(String)
    password = Column(String)
    membership_type = Column(String)
    Clinical_history = Column(Integer)
    created_date = Column(Date, default=datetime.utcnow)
