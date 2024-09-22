from typing import Optional
from pydantic import BaseModel, Field
from datetime import date


class Ips_schema(BaseModel):

    id: Optional[int] = None
    name_hospital: str = Field()
    city: str = Field()
    Address: str = Field()
    email: str = Field()
    create_by: int = Field()
    phone_number: str = Field()


class Ips_update(BaseModel):

    email: str = Field()
    phone_number: str = Field()
