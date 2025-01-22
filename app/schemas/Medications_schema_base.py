from typing import Optional
from pydantic import BaseModel, Field


class Medications_schema(BaseModel):
    """
    esta clase permite la entrada de datos em un formato para la base de datos de Medications_model,
    esto con el fin para evitar errores al momento de insertar registros en la base de datos, 
    tambien se especifica el tipo de dato que se necesita
    """
    generic_name: str = Field()
    dose: int = Field()
    price: int = Field()
    contraindications: str = Field()
    created_by: str = Field()
    Stocks: int = Field()


class Medications_update(BaseModel):
    """
    esta clase permite la entrada de datos em un formato para la base de datos de Medications_model,
    esto con el fin para evitar errores al momento de insertar registros en la base de datos, 
    tambien se especifica el tipo de dato que se necesita
    """
    dose: int = Field()
    price: int = Field()
    contraindications: str = Field()
    aviable: bool = Field()
    Stocks: str = Field()


class Medications_user(BaseModel):
    """
    esta clase permite la entrada de datos em un formato para la base de datos de Medications_model,
    esto con el fin para evitar errores al momento de insertar registros en la base de datos, 
    tambien se especifica el tipo de dato que se necesita
    """
    user_money: int = Field()
    Stocks: int = Field()


class medicatios_filter_schema(BaseModel):

    """
    con esta clase se permite ver las opciones por las cuales se puede filtar,
    con esto se pasa para el registro y asi se hace la busqueda
    """

    id: Optional[int] = Field(default="")
    generic_name: Optional[str] = Field(default="")
    price: Optional[int] = Field(default="")
