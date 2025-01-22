from typing import Optional
from pydantic import BaseModel, Field
from datetime import date, time


class medical_appointments_schema(BaseModel):
    """
    esta clase permite la entrada de datos em un formato para la base de datos de medical_appointments_schema_model,
    esto con el fin para evitar errores al momento de insertar registros en la base de datos, 
    tambien se especifica el tipo de dato que se necesita
    """

    appointment_type: str = Field()
    fullname_affiliate: str = Field()
    document_number_affiliate: int = Field()
    name_doctor: str = Field()
    created_by: str = Field()
    day: date = Field()
    hospital_name: str = Field()
    Clinical_history: int = Field()
    hour: time = Field()


class update_appoinments_schema(BaseModel):
    """
    esta clase permite la entrada de datos em un formato para la base de datos de Medications_model,
    esto con el fin para evitar errores al momento de insertar registros en la base de datos, 
    tambien se especifica el tipo de dato que se necesita
    """
    name_doctor: str = Field()
    hour: int = Field()
    day: int = Field()


class fliter_appoinments_schema(BaseModel):
    """
    con esta clase se permite ver las opciones por las cuales se puede filtar,
    con esto se pasa para el registro y asi se hace la busqueda
    """
    id: Optional[int] = None
    document_number_affiliate: Optional[int] = None
    name_doctor: Optional[str] = None
    day: Optional[date] = None
    hospital_name: Optional[str] = None
