from schemas.Specialist_schemas import Specialist_schema, Specialist_update
from config.db import Session
from middleware.jwt_bear import JWTBearer
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from services.Specialist_service import specialist_service
from fastapi import APIRouter, Depends

specialist_router = APIRouter()


@specialist_router.post("/create/specialist", tags=["CRUD SPECIALIST"], dependencies=[Depends(JWTBearer())])
async def create_specialist(specialist: Specialist_schema):
    """
    esta funcion crea un registro de tipo espicialista utilizando el archivo en el paquete de schema,
    con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
    seguridad ya que los afiliados  tienen varios permisos, luego de valiadar, si el token no es correcto
    retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
    """
    db = Session()
    result = specialist_service(db).create_specialist(specialist)
    return JSONResponse(content={"mensage": "el especialista se ha registrado"})


@specialist_router.get("/all/specialist", tags=["CRUD SPECIALIST"], dependencies=[Depends(JWTBearer())])
async def get_all_specialist():
    """
    esta funcion trear todos los  registro de la base de datos de  especialista,
    con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
    seguridad ya que los admins tienen varios permisos, luego de valiadar, si el token no es correcto
    retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
    """
    db = Session()
    result = specialist_service(db).get_specialist()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@specialist_router.put("/update/specialist", tags=["CRUD SPECIALIST"], dependencies=[Depends(JWTBearer())])
async def update_specialist(document_number: int, ips: Specialist_update):
    """
    esta funcion actualiza un registro de tipo especialista utilizando el archivo en el paquete de schema,
    con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
    seguridad ya que los admins tienen varios permisos, luego de valiadar, si el token no es correcto
    retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
    """
    db = Session()
    result = specialist_service(db).update_specialist(document_number, ips)
    return JSONResponse(status_code=200, content={"mensage": "el especialista ha sido actualizado"})


@specialist_router.delete("/dalete/specialist", tags=["CRUD SPECIALIST"], dependencies=[Depends(JWTBearer())])
async def delete_specialist(document_number: int):
    """
    esta funcion eliminar un registro de tipo medications,
    con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
    seguridad ya que los admins tienen varios permisos, luego de valiadar, si el token no es correcto
    retorna un error, pero si si, verifica los datos y sin son validos retornara que el usuario ha sido eliminado
    """
    db = Session()
    result = specialist_service(db).delete_specialist(document_number)
    return JSONResponse(status_code=200, content={"mensage": "el especialista ha sido eliminados"})
