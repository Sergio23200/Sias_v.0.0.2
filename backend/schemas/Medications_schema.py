from typing import Optional
from pydantic import BaseModel, Field
from datetime import date


class Medications(BaseModel):
    id = Optional[int] = None
    generic_name: str = Field()
    dose: int = Field()
    price: int = Field()
    contraindications: str = Field()
    created_by: str = Field()
    aviable: bool = Field()
    Stocks: str = Field()
