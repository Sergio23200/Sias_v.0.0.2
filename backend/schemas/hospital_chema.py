from typing import Optional
from pydantic import BaseModel, Field
from datetime import date


class Hospital_schema(BaseModel):

    id: Optional[int] = None
    name_hospital: str = Field()
    city: str = Field()
    Address: str = Field()
    email: str = Field()
    phone_number: str = Field()
    ambulance_dispo: str = Field()
    ambulances_on_route: int = Field()
    create_by: int = Field()


class Hospital_update(BaseModel):

    email: str = Field()
    phone_number: str = Field()
    ambulance_dispo: str = Field()
    ambulances_on_route: int = Field()
