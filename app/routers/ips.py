from schemas.Ips_schema import Ips_schema, Ips_update, ips_filter_schema
from config.db import Session
from fastapi.responses import JSONResponse
from services.admin_services import Admin_service
from middleware.jwt_bear import JWTBearer
from fastapi.encoders import jsonable_encoder
from utils.jwt_manger import validate_token
from typing import Optional
from services.ips_services import ips_service
from fastapi import APIRouter, Depends, Query

ips_router = APIRouter()
db = Session()


@ips_router.get("/all/ips", tags=["CRUD IPS"], dependencies=[Depends(JWTBearer())])
async def get_all_ips(token: str = Depends(JWTBearer())):
    """
    esta funcion trear todos los  registro de la base de datos de  ips
    con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
    seguridad ya que los admin tienen varios permisos, luego de valiadar, si el token no es correcto
    retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
    """
    payload = validate_token(token)
    email = payload.get("email")
    validate = Admin_service(db).validate_admin(email)
    if not validate:
        return JSONResponse(content={"mensage": "el usuario no tiene permisos"})
    result = ips_service(db).get_ips()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@ips_router.get("/filter/ips", tags=["CRUD IPS"], dependencies=[Depends(JWTBearer())])
async def get_filter_ips(id: Optional[int] = Query(None),
                         name_hospital: Optional[str] = Query(None),
                         city: Optional[str] = Query(None),
                         Address: Optional[str] = Query(None),
                         email_f: Optional[str] = Query(None),
                         phone_number: Optional[int] = Query(None),
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
    filters = ips_filter_schema(id=id, name_hospital=name_hospital, city=city,
                                Address=Address, email=email_f, phone_number=phone_number)
    result = ips_service(db).get_ips_filter(valor=filters)
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@ips_router.post("/create/ips", tags=["CRUD IPS"], dependencies=[Depends(JWTBearer())])
async def create_ips(ips: Ips_schema, token: str = Depends(JWTBearer())):
    """
    esta funcion crea un registro de tipo ips utilizando el archivo en el paquete de schema,
    con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
    seguridad ya que los admins tienen varios permisos, luego de valiadar, si el token no es correcto
    retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
    """
    payload = validate_token(token)
    email = payload.get("email")
    validate = Admin_service(db).validate_admin(email)
    if not validate:
        return JSONResponse(content={"mensage": "el usuario no tiene permisos"})
    ips_service(db).create_ips(ips)
    return JSONResponse(content={"mensage": "la ips se ha registrado"})


@ips_router.put("/update/ips", tags=["CRUD IPS"], dependencies=[Depends(JWTBearer())])
async def update_ips(name_hospital: str, ips: Ips_update, token: str = Depends(JWTBearer())):
    """
    esta funcion actualiza un registro de tipo admin utilizando el archivo en el paquete de schema,
    con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
    seguridad ya que los admins tienen varios permisos, luego de valiadar, si el token no es correcto
    retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
    """
    payload = validate_token(token)
    email = payload.get("email")
    validate = Admin_service(db).validate_admin(email)
    if not validate:
        return JSONResponse(content={"mensage": "el usuario no tiene permisos"})
    result = ips_service(db).update_ips(name_hospital, ips)
    return JSONResponse(status_code=200, content={"mensage": "la ips ha sido actualizado"})


@ips_router.delete("/dalete/ips", tags=["CRUD IPS"], dependencies=[Depends(JWTBearer())])
async def delete_ips(name_hospital: str, token: str = Depends(JWTBearer())):
    """
    esta funcion eliminar un registro de tipo ips,
    con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
    seguridad ya que los admins tienen varios permisos, luego de valiadar, si el token no es correcto
    retorna un error, pero si si, verifica los datos y sin son validos retornara que el usuario ha sido eliminado
    """
    payload = validate_token(token)
    email = payload.get("email")
    validate = Admin_service(db).validate_admin(email)
    if not validate:
        return JSONResponse(content={"mensage": "el usuario no tiene permisos"})
    result = ips_service(db).delete_ips(name_hospital)
    return JSONResponse(status_code=200, content={"mensage": "la ips ha sido eliminados"})
