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


class medicatios_filter_schema(BaseModel):

    """

    esta funcion crea un registro de tipo medications utilizando el archivo en el paquete de schema,
    con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
    seguridad ya que los afiliados  tienen varios permisos, luego de valiadar, si el token no es correcto
    retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado 
           
    """

    id: Optional[int] = None
    generic_name: Optional[str] = Field()
    price: Optional[int] = Field()
