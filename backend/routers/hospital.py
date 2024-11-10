from schemas.hospital_chema import Hospital_schema, Hospital_update, hospital_filter_schema
from config.db import Session
from services.admin_services import Admin_service
from middleware.jwt_bear import JWTBearer
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from middleware.jwt_bear import validate_token
from typing import Optional
from services.hospital_service import hospìtal_service
from fastapi import APIRouter, Depends, Query

hospital_router = APIRouter()
db = Session()


@hospital_router.get("/all/hospital", tags=["CRUD HOSPITAL"], dependencies=[Depends(JWTBearer())])
async def get_all_hospital(token: str = Depends(JWTBearer())):
    """
    esta funcion trear todos los  registro de la base de datos de  hospitales,
    con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
    seguridad ya que los admins tienen varios permisos, luego de valiadar, si el token no es correcto
    retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
    """
    payload = validate_token(token)

    email = payload.get("email")
    validate = Admin_service(db).validate_admin(email)
    if not validate:
        return JSONResponse(content={"mensage": "el usuario no tiene permisos"})
    result = hospìtal_service(db).get_hospital()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@hospital_router.get("/filters/hospital",  tags=["CRUD HOSPITAL"], dependencies=[Depends(JWTBearer())])
async def get_filters_hospital(id: Optional[int] = Query(None),
                               name_hospital: Optional[str] = Query(None),
                               city: Optional[str] = Query(None),
                               Address: Optional[str] = Query(None),
                               email_f: Optional[str] = Query(None),
                               phone_number: Optional[str] = Query(None),
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
    if not validate:
        return JSONResponse(content={"mensage": "el usuario no tiene permisos"})
    filters = hospital_filter_schema(
        id=id, name_hospital=name_hospital, phone_number=phone_number, city=city, Address=Address, email=email_f)
    result = hospìtal_service(db).get_hospital_filter(valor=filters)
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@hospital_router.post("/create/hospital", tags=["CRUD HOSPITAL"], dependencies=[Depends(JWTBearer())])
async def create_hospital(hospital: Hospital_schema, token: str = Depends(JWTBearer())):
    """
    esta funcion crea un registro de tipo hospital utilizando el archivo en el paquete de schema,
    con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
    seguridad ya que los admins tienen varios permisos, luego de valiadar, si el token no es correcto
    retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
    """

    payload = validate_token(token)
    email = payload.get("email")
    validate = Admin_service(db).validate_admin(email)
    if not validate:
        return JSONResponse(content={"mensage": "el usuario no tiene permisos"})
    hospìtal_service(db).create_hospital(hospital)
    return JSONResponse(content={"mensage": "el hospital se ha registrado"})


@hospital_router.put("/update/hospital", tags=["CRUD HOSPITAL"], dependencies=[Depends(JWTBearer())])
async def update_hospital(name_hospital: int, hospital: Hospital_update, token: str = Depends(JWTBearer())):
    """
    esta funcion actualiza un registro de tipo hospital utilizando el archivo en el paquete de schema,
    con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
    seguridad ya que los admins tienen varios permisos, luego de valiadar, si el token no es correcto
    retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
    """
    payload = validate_token(token)
    email = payload.get("email")
    validate = Admin_service(db).validate_admin(email)
    if not validate:
        return JSONResponse(content={"mensage": "el usuario no tiene permisos"})
    result = hospìtal_service(db).update_hospital(name_hospital, hospital)
    return JSONResponse(status_code=200, content={"mensage": "EL hospital ha sido actualizado"})


@hospital_router.delete("/dalete/hospital", tags=["CRUD HOSPITAL"], dependencies=[Depends(JWTBearer())])
async def delete_hospital(name_hospital: str, token: str = Depends(JWTBearer())):
    """
    esta funcion eliminar un registro de tipo hospital,
    con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
    seguridad ya que los admins tienen varios permisos, luego de valiadar, si el token no es correcto
    retorna un error, pero si si, verifica los datos y sin son validos retornara que el usuario ha sido eliminado
    """
    payload = validate_token(token)
    email = payload.get("email")
    validate = Admin_service(db).validate_admin(email)
    if not validate:
        return JSONResponse(content={"mensage": "el usuario no tiene permisos"})
    result = hospìtal_service(db).delete_hospital(name_hospital)
    return JSONResponse(status_code=200, content={"mensage": "el hospital ha sido eliminados"})
