from typing import Optional
from pydantic import BaseModel, Field


class Medications_schema(BaseModel):
    """
    esta clase permite la entrada de datos em un formato para la base de datos de Medications_model,
    esto con el fin para evitar errores al momento de insertar registros en la base de datos, 
    tambien se especifica el tipo de dato que se necesita
    """
    id: Optional[int] = None
    generic_name: str = Field()
    dose: int = Field()
    price: int = Field()
    contraindications: str = Field()
    created_by: str = Field()
    aviable: bool = Field()
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
    user_money: float = Field(..., description="Amount of money the user has")
    Stocks: int = Field(..., description="Amount of stocks the user holds")
