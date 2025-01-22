from typing import Optional
from pydantic import BaseModel, Field
from datetime import date


class Ips_schema(BaseModel):
    """
    esta clase permite la entrada de datos em un formato para la base de datos de Ips_model,
    esto con el fin para evitar errores al momento de insertar registros en la base de datos, 
    tambien se especifica el tipo de dato que se necesita
    """

    name_hospital: str = Field()
    city: str = Field()
    Address: str = Field()
    email: str = Field()
    create_by: int = Field()
    phone_number: str = Field()
    create_by: int = Field()


class Ips_update(BaseModel):
    """
    esta clase permite la entrada de datos em un formato para la base de datos de Ips_model,
    esto con el fin para evitar errores al momento de insertar registros en la base de datos, 
    tambien se especifica el tipo de dato que se necesita
    """
    email: str = Field()
    phone_number: str = Field()


class ips_filter_schema(BaseModel):
    """
    esta funcion crea un registro de tipo medications utilizando el archivo en el paquete de schema,
    con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
    seguridad ya que los afiliados  tienen varios permisos, luego de valiadar, si el token no es correcto
    retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
    """
    id: Optional[int] = Field()
    name_hospital: Optional[str] = Field()
    city: Optional[str] = Field()
    Address: Optional[str] = Field()
    email: Optional[str] = Field()
    phone_number: Optional[str] = Field()
