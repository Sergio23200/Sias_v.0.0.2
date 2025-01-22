from typing import Optional
from pydantic import BaseModel, Field


class Medications_user_schema(BaseModel):
    """
    esta clase permite la entrada de datos em un formato para la base de datos de Medications_model,
    esto con el fin para evitar errores al momento de insertar registros en la base de datos, 
    tambien se especifica el tipo de dato que se necesita
    """

    generic_name: str = Field()
    Stocks: int = Field()
    affiliate: str = Field()


class Medications_user_filter_schema(BaseModel):
    """
    con esta clase se permite ver las opciones por las cuales se puede filtar,
    con esto se pasa para el registro y asi se hace la busqueda
    """

    id: Optional[int] = Field(default="")
    generic_name: Optional[str] = Field(default="")
    fullname_user: Optional[str] = Field(default="")
