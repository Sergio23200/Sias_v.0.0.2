from typing import Optional
from pydantic import BaseModel, Field
from datetime import date


class Admin_schema(BaseModel):
    """
    esta clase permite la entrada de datos em un formato para la base de datos de admin_model,
    esto con el fin para evitar errores al momento de insertar registros en la base de datos, 
    tambien se especifica el tipo de dato que se necesita
    """
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
