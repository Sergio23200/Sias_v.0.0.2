
from typing import Optional
from pydantic import BaseModel, Field
from datetime import date


class Affiliate_schema(BaseModel):
    """
    esta clase permite la entrada de datos em un formato para la base de datos de Affiliate_model,
    esto con el fin para evitar errores al momento de insertar registros en la base de datos, 
    tambien se especifica el tipo de dato que se necesita
    """

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


class filter_afiliate_schema(BaseModel):
    """
    con esta clase se permite ver las opciones por las cuales se puede filtar,
    con esto se pasa para el registro y asi se hace la busqueda
    """
    id: Optional[int] = Field(default="")
    document_number: Optional[int] = Field(default="")
    email: Optional[str] = Field(default="")
    Clinical_history: Optional[int] = Field(default="")
    city:  Optional[str] = Field(default="")


class LoginChatbotRequest(BaseModel):
    type_document: str
    document_number: int
    email: str


class return_afiliate(BaseModel):
    fullname: str
    document_number: int
    birthdate: date
    membership_type: str
