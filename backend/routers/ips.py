from schemas.Ips_schema import Ips_schema, Ips_update
from config.db import Session
from fastapi.responses import JSONResponse
from middleware.jwt_bear import JWTBearer
from fastapi.encoders import jsonable_encoder
from services.ips_services import ips_service
from fastapi import APIRouter, Depends

ips_router = APIRouter()


@ips_router.post("/create/ips", tags=["CRUD IPS"], dependencies=[Depends(JWTBearer())])
async def create_ips(ips: Ips_schema):
    """
    esta funcion crea un registro de tipo ips utilizando el archivo en el paquete de schema,
    con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
    seguridad ya que los admins tienen varios permisos, luego de valiadar, si el token no es correcto
    retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
    """
    db = Session()
    ips_service(db).create_ips(ips)
    return JSONResponse(content={"mensage": "la ips se ha registrado"})


@ips_router.get("/all/ips", tags=["CRUD IPS"], dependencies=[Depends(JWTBearer())])
async def get_all_ips():
    """
    esta funcion trear todos los  registro de la base de datos de  ips
    con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
    seguridad ya que los admin tienen varios permisos, luego de valiadar, si el token no es correcto
    retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
    """
    db = Session()
    result = ips_service(db).get_ips()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@ips_router.put("/update/ips", tags=["CRUD IPS"], dependencies=[Depends(JWTBearer())])
async def update_ips(name_hospital: str, ips: Ips_update):
    """
    esta funcion actualiza un registro de tipo admin utilizando el archivo en el paquete de schema,
    con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
    seguridad ya que los admins tienen varios permisos, luego de valiadar, si el token no es correcto
    retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
    """
    db = Session()
    result = ips_service(db).update_ips(name_hospital, ips)
    return JSONResponse(status_code=200, content={"mensage": "la ips ha sido actualizado"})


@ips_router.delete("/dalete/ips", tags=["CRUD IPS"], dependencies=[Depends(JWTBearer())])
async def delete_ips(name_hospital: str):
    """
    esta funcion eliminar un registro de tipo ips,
    con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
    seguridad ya que los admins tienen varios permisos, luego de valiadar, si el token no es correcto
    retorna un error, pero si si, verifica los datos y sin son validos retornara que el usuario ha sido eliminado
    """
    db = Session()
    result = ips_service(db).delete_ips(name_hospital)
    return JSONResponse(status_code=200, content={"mensage": "la ips ha sido eliminados"})
