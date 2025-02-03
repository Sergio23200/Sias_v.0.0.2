from typing import Optional
from pydantic import BaseModel, Field
from datetime import date


class Admin_schema(BaseModel):
    """
    esta clase permite la entrada de datos em un formato para la base de datos de admin_model,
    esto con el fin para evitar errores al momento de insertar registros en la base de datos, 
    tambien se especifica el tipo de dato que se necesita
    """
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
    """
    esta clase permite la entrada de datos em un formato para la base de datos de admin_model,
    esto con el fin para evitar errores al momento de insertar registros en la base de datos, 
    tambien se especifica el tipo de dato que se necesita
    """
    email: str = Field()
    first_number: str = Field()
    city: str = Field()
    password: str = Field()
    job_title: str = Field()


class admin_filter_schema(BaseModel):
    """
    con esta clase se permite ver las opciones por las cuales se puede filtar,
    con esto se pasa para el registro y asi se hace la busqueda
    """
    id: Optional[int] = Field(default="")
    fullname: Optional[str] = Field(default="")
    document_number:  Optional[int] = Field(default="")
    email:  Optional[str] = Field(default="")
    city:  Optional[str] = Field(default="")
    job_title:  Optional[str] = Field(default="")
