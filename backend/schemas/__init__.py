from typing import Optional
from pydantic import BaseModel, Field
from datetime import date, time


class Affiliate(BaseModel):
    id: Optional[int] = None
    fullname: str = Field()
    document_type: str = Field()
    document_number: int = Field()
    birthdate: date = Field()
    gender: str = Field()
    email: str = Field()
    Address: str = Field()
    Clinical_history: int = Field()
    phone_number: int = Field()
    city:  str = Field()
    password: str = Field()
    membership_type: str = Field()

    class Meta:
        database = (BaseModel)
        db_table = 'Affiliate'


class admin(BaseModel):
    id = Optional[int] = None
    fullname: str = Field()
    document_type: str = Field()
    document_number: int = Field()
    birthdate: str = Field()
    email: str = Field()
    first_number: str = Field()
    city: int = Field()
    password: str = Field
    job_title: str = Field()
    
    class Meta:
        database = (BaseModel)
        db_table = 'Admin'


class medical_appointments(BaseModel):
    id = Optional[int] = None
    appointment_type: str = Field()
    fullname_affiliate: str = Field()
    document_number_affiliate: int = Field()
    name_doctor: str = Field()
    created_by: str = Field()
    day: int = Field()
    hospital_name: str = Field()
    Clinical_history: int = Field()
    hour: int = Field()

    class Meta:
        database = (BaseModel)
        db_table = 'medical_appointments'


class Specialist(BaseModel):
    id = Optional[int] = None
    fullname: str = Field()
    number_document: int = Field()
    email: str = Field()
    phone_number: int = Field()
    specialty: str = Field()
    created_by: str = Field()


    class Meta:
        database = (BaseModel)
        db_table = "Specialist"


class Hospital(BaseModel):
    id = Optional[int] = None
    fullname: str = Field()
    Address: str = Field()
    email: str = Field()
    phone_number: int = Field()
    ambulance_dispo: str = Field()
    ambulances_on_route: str = Field()
    created_by: str = Field()


    class Meta:
        database = (BaseModel) 
        db_table = "Hospital"


class Ips(BaseModel):
    id = Optional[int] = None
    fullname: str = Field()
    city:  str = Field()
    Address: str = Field()
    phone_number: int = Field()
    created_by: str = Field()

    class Meta:
        database = (BaseModel)
        db_table = "Health_Centers"


class Medications(BaseModel):
    id = Optional[int] = None
    generic_name: str = Field()
    dose: int = Field()
    price: int = Field()
    contraindications: str = Field()
    created_by: str = Field() 
    aviable: bool = Field()
    Stocks: str = Field()

    class Meta:
        database = (BaseModel)
        db_table = "Medications"


if __name__ == "__main__":
    BaseModel.connect()  
    BaseModel.create_tables([Affiliate, admin, medical_appointments,
                           Specialist, Hospital, Ips, Medications])
    BaseModel.close()     
