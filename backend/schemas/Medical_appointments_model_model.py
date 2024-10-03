from typing import Optional
from pydantic import BaseModel, Field
from datetime import date


class medical_appointments_schema(BaseModel):
    """
    esta clase permite la entrada de datos em un formato para la base de datos de medical_appointments_schema_model,
    esto con el fin para evitar errores al momento de insertar registros en la base de datos, 
    tambien se especifica el tipo de dato que se necesita
    """
    id = Optional[int] = None
    appointment_type: str = Field()
    fullname_affiliate: str = Field()
    document_number_affiliate: int = Field()
    name_doctor: str = Field()
    created_by: str = Field()
    day: int = Field()
    hospital_name: str = Field()
    Clinical_history: int = Field()
    hour: int = Field()
