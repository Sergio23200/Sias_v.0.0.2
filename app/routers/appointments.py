from services.medical_appointments_services import appoinments_service
from services.affiliate_services import Affiliate_service
from schemas.Medical_appointment_schema import fliter_appoinments_schema, medical_appointments_schema, update_appoinments_schema
from services.admin_services import Admin_service
from services.Specialist_service import specialist_service
from services.hospital_service import hospìtal_service
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from datetime import date
from config.db import Session
from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from utils.jwt_manger import validate_token
from middleware.jwt_bear import JWTBearer

appointments_router = APIRouter()
db = Session()


@appointments_router.get("/all/appointments", tags=["CRUD APPOINSTMENTS"], dependencies=[Depends(JWTBearer())])
async def get_all_appointments(token: str = Depends(JWTBearer())):
    """
    esta funcion trear todos los  registro de la base de datos de  appointments,
    con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
    seguridad ya que los admins tienen varios permisos, luego de valiadar, si el token no es correcto
    retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
    """
    payload = validate_token(token)
    email = payload.get("email")
    validate = Admin_service(db).validate_admin(email)
    if not validate:
        return JSONResponse(content={"mensage": "el usuario no tiene permisos"})
    result = appoinments_service(db).get_appoinment()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@appointments_router.get("/filter/appointments", tags=["CRUD APPOINSTMENTS"], dependencies=[Depends(JWTBearer())])
async def get_filter_medications(id: Optional[int] = Query(None),
                                 document_number_affiliate: Optional[int] = Query(
                                     None),
                                 name_doctor: Optional[str] = Query(None),
                                 day: Optional[date] = Query(None),
                                 hospital_name: Optional[str] = Query(None),
                                 token: str = Depends(JWTBearer())):
    """
    esta funcion trear todos los  registro de la base de datos de  afiliado
    con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
    seguridad ya que los afiliados tienen varios permisos, luego de valiadar, si el token no es correcto
    retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
    """
    payload = validate_token(token)
    email = payload.get("email")
    validate = Admin_service(db).validate_admin(email)
    filters = fliter_appoinments_schema(
        id=id,
        document_number_affiliate=document_number_affiliate,
        name_doctor=name_doctor,
        day=day,
        hospital_name=hospital_name
    )
    result = appoinments_service(db).get_appoinments_filter(filters)
    if not validate:
        return JSONResponse(content={"mensage": "el usuario no tiene permisos"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@appointments_router.post("/filter/appointments", tags=["CRUD APPOINSTMENTS"], dependencies=[Depends(JWTBearer())])
async def create_appointments(data: medical_appointments_schema, token: str = Depends(JWTBearer())):
    """
    esta funcion crea un registro de tipo hospital utilizando el archivo en el paquete de schema,
    con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
    seguridad ya que los admins tienen varios permisos, luego de valiadar, si el token no es correcto
    retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
    """
    ver_doc = Affiliate_service(db).verificate_doc(
        document_number=data.document_number_affiliate)
    ver_name_doc = specialist_service(db).verif_name(fullname=data.name_doctor)
    vec_name_hos = hospìtal_service(db).vec_name_hospital(
        name_hospital=data.hospital_name)
    if not ver_doc:
        return JSONResponse(content={"mensage": "el usuario no esta registrado"})
    elif not ver_name_doc:
        return JSONResponse(content={"mensage": "el doctor no esta registrado"})
    elif not vec_name_hos:
        return JSONResponse(content={"mensage": "el hospitañ no esta registrado"})
    appoinments_service(db).create_appoinments(data)
    return JSONResponse(content={"mensage": "la cita  se ha registrado"})
