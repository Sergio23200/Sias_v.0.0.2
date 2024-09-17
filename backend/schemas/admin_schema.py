from typing import Optional
from pydantic import BaseModel, Field
from datetime import date


class Admin_schema(BaseModel):
    id: Optional[int] = None
    fullname: str = Field()
    document_type: str = Field()
    document_number: int = Field()
    birthdate: date = Field()
    email: str = Field()
    first_number: str = Field()
    city: str = Field()
    password: str = Field()
    job_title: str = Field()


class Admin_update(BaseModel):
    email: str = Field()
    first_number: str = Field()
    city: str = Field()
    password: str = Field()
    job_title: str = Field()
