
from typing import Optional
from pydantic import BaseModel, Field
from datetime import date


class Affiliate_schema(BaseModel):
    """
    esta clase permite la entrada de datos em un formato para la base de datos de Affiliate_model,
    esto con el fin para evitar errores al momento de insertar registros en la base de datos, 
    tambien se especifica el tipo de dato que se necesita
    """
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


class affilate_update(BaseModel):
    """
    esta clase permite la entrada de datos em un formato para la base de datos de Affiliate_model,
    esto con el fin para evitar errores al momento de insertar registros en la base de datos, 
    tambien se especifica el tipo de dato que se necesita
    """
    email: str = Field()
    Address: str = Field()
    phone_number: int = Field()
    city:  str = Field()
    password: str = Field()
    membership_type: str = Field()
