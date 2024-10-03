from schemas.Medications_schema_base import Medications_schema, Medications_update, Medications_user
from config.db import Session
from fastapi.responses import JSONResponse
from middleware.jwt_bear import JWTBearer
from fastapi.encoders import jsonable_encoder
from services.Medications_service import Medications_service
from fastapi import APIRouter, Depends

medications_router = APIRouter()


@medications_router.post("/create/medications", tags=["CRUD MEDICATIONS"], dependencies=[Depends(JWTBearer())])
async def create_medications(medications: Medications_schema):
    """
    esta funcion crea un registro de tipo medications utilizando el archivo en el paquete de schema,
    con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
    seguridad ya que los afiliados  tienen varios permisos, luego de valiadar, si el token no es correcto
    retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
    """
    db = Session()
    result = Medications_service(db).create_medications(medications)
    return JSONResponse(content={"mensage": "el medicamento se ha registrado"})


@medications_router.get("/all/medications", tags=["CRUD MEDICATIONS"], dependencies=[Depends(JWTBearer())])
async def get_all_medications():
    """
    esta funcion trear todos los  registro de la base de datos de  medications,
    con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
    seguridad ya que los admins tienen varios permisos, luego de valiadar, si el token no es correcto
    retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
    """
    db = Session()
    result = Medications_service(db).get_medications()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@medications_router.put("/update/medications", tags=["CRUD MEDICATIONS"], dependencies=[Depends(JWTBearer())])
async def update_medications(generic_name: str, ips: Medications_update):
    """
    esta funcion actualiza un registro de tipo medications utilizando el archivo en el paquete de schema,
    con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
    seguridad ya que los admins tienen varios permisos, luego de valiadar, si el token no es correcto
    retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
    """
    db = Session()
    result = Medications_service(db).update_medications(generic_name, ips)
    return JSONResponse(status_code=200, content={"mensage": "el medicamento ha sido actualizado"})


@medications_router.delete("/dalete/medications", tags=["CRUD MEDICATIONS"], dependencies=[Depends(JWTBearer())])
async def delete_medications(generic_name: str):
    """
    esta funcion eliminar un registro de tipo medications,
    con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
    seguridad ya que los admins tienen varios permisos, luego de valiadar, si el token no es correcto
    retorna un error, pero si si, verifica los datos y sin son validos retornara que el usuario ha sido eliminado
    """
    db = Session()
    result = Medications_service(db).delete_medications(generic_name)
    return JSONResponse(status_code=200, content={"mensage": "el medicamento ha sido eliminados"})


@medications_router.put("/user/medications", tags=["CRUD MEDICATIONS"], dependencies=[Depends(JWTBearer())])
async def user_medication(data: Medications_user, generic_name: str):
    """
    esta funcion actualiza un registro de tipo medications utilizando el archivo en el paquete de schema,
    con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
    seguridad ya que los admins tienen varios permisos, luego de valiadar, si el token no es correcto
    retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
    """
    db = Session()
    result = Medications_service(db).user_medications(generic_name, data)
    return result
