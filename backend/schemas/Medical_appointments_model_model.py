from typing import Optional
from pydantic import BaseModel, Field
from datetime import date


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
