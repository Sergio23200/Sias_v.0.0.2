from typing import Optional
from pydantic import BaseModel, Field
from datetime import date


class Specialist_schema(BaseModel):
    """
    esta clase permite la entrada de datos em un formato para la base de datos de Specialist_model,
    esto con el fin para evitar errores al momento de insertar registros en la base de datos, 
    tambien se especifica el tipo de dato que se necesita
    """

    fullname: str = Field()
    number_document: int = Field()
    email: str = Field()
    phone_number: str = Field()
    specialty: str = Field()
    created_by: int = Field()


class Specialist_update(BaseModel):
    """
    esta clase permite la entrada de datos em un formato para la base de datos de Specialist_model,
    esto con el fin para evitar errores al momento de insertar registros en la base de datos, 
    tambien se especifica el tipo de dato que se necesita
    """

    email: str = Field()
    phone_number: str = Field()
    specialty: str = Field()


class specialistr_filter_schema(BaseModel):
    """
    con esta clase se permite ver las opciones por las cuales se puede filtar,
    con esto se pasa para el registro y asi se hace la busqueda
    """

    id: Optional[int] = Field(default="")
    fullname: Optional[str] = Field(default="")
    number_document: Optional[str] = Field(default="")
    email: Optional[str] = Field(default="")
    phone_number: Optional[str] = Field(default="")
    specialty: Optional[str] = Field(default="")
