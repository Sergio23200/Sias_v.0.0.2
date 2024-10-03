from typing import Optional
from pydantic import BaseModel, Field
from datetime import date


class Hospital_schema(BaseModel):
    """
    esta clase permite la entrada de datos em un formato para la base de datos de Hospitale_model,
    esto con el fin para evitar errores al momento de insertar registros en la base de datos, 
    tambien se especifica el tipo de dato que se necesita
    """

    id: Optional[int] = None
    name_hospital: str = Field()
    city: str = Field()
    Address: str = Field()
    email: str = Field()
    phone_number: str = Field()
    ambulance_dispo: str = Field()
    ambulances_on_route: int = Field()
    create_by: int = Field()


class Hospital_update(BaseModel):
    """
    esta clase permite la entrada de datos em un formato para la base de datos de Hospitale_model,
    esto con el fin para evitar errores al momento de insertar registros en la base de datos, 
    tambien se especifica el tipo de dato que se necesita
    """
    email: str = Field()
    phone_number: str = Field()
    ambulance_dispo: str = Field()
    ambulances_on_route: int = Field()
