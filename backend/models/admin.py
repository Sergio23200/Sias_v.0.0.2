from config.db import Base
from datetime import datetime
from sqlalchemy import Column, Integer, String, Date


class Admin_model(Base):
    __tablename__ = "Admin"

    id = Column(Integer, primary_key=True)
    fullname = Column(String)
    document_type = Column(String)
    document_number = Column(Integer)
    birthdate = Column(Date)
    email = Column(String)
    first_number = Column(String)
    city = Column(String)
    password = Column(String)
    job_title = Column(String)
    created_date = Column(Date, default=datetime.utcnow)
