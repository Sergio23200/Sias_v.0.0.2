from typing import Optional
from pydantic import BaseModel, Field
from datetime import date


class Specialist_model(BaseModel):

    id: Optional[int] = None
    fullname: str = Field()
    number_document: int = Field()
    email: str = Field()
    phone_number: str = Field()
    specialty: str = Field()
    created_by: int = Field()
