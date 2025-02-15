from schemas.admin_schema import Admin_schema, Admin_update, admin_filter_schema
from services.admin_services import Admin_service
from config.db import Session
from typing import Optional
from utils.jwt_manger import validate_token
from middleware.jwt_bear import JWTBearer
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Depends, Query


admin_router = APIRouter()
db = Session()


@admin_router.post("/create/admin", tags=["CRUD ADMIN"])
async def create_admin(admin: Admin_schema):
    """
    esta funcion crea un registro de tipo admin utilizando el archivo en el paquete de schema,
    con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
    seguridad ya que los admins tienen varios permisos, luego de valiadar, si el token no es correcto
    retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
    """

    a = Admin_service(db).create_Admin(admin)
    if not a:
        return JSONResponse(content={"mensage": "el usuario no tiene los datos necesarios"})
    return a


@admin_router.get("/all/admin", tags=["CRUD ADMIN"], dependencies=[Depends(JWTBearer())])
async def get_all_admin(token: str = Depends(JWTBearer())):
    """
    esta funcion trear todos los  registro de la base de datos de  admin,
    con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
    seguridad ya que los admins tienen varios permisos, luego de valiadar, si el token no es correcto
    retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
    """
    payload = validate_token(token)
    email = payload.get("email")
    validate = Admin_service(db).validate_admin(email)
    if not validate:
        return JSONResponse(content={"mensage": "el usuario no tiene permisos"})

    result = Admin_service(db).get_admin()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@admin_router.get("/filters/admin", tags=["CRUD ADMIN"], dependencies=[Depends(JWTBearer())])
async def get_fliter(fullname: Optional[str] = Query(None),
                     id: Optional[str] = Query(None),
                     email_f: Optional[str] = Query(None),
                     document_number: Optional[str] = Query(None),
                     city: Optional[str] = Query(None),
                     job_title: Optional[str] = Query(None),
                     token: str = Depends(JWTBearer())):
    """
    esta funcion trear todos los  registro de la base de datos de  admin,
    con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
    seguridad ya que los admins tienen varios permisos, luego de valiadar, si el token no es correcto
    retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
    """
    payload = validate_token(token)
    email = payload.get("email")
    filters = admin_filter_schema(
        id=id, fullname=fullname, email=email_f, document_number=document_number, city=city, job_title=job_title)
    validate = Admin_service(db).validate_admin(email)
    if not validate:
        return JSONResponse(content={"mensage": "el usuario no tiene permisos"})

    result = Admin_service(db).get_admin_filter(filters)
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@admin_router.put("/update/admin", tags=["CRUD ADMIN"])
async def update_admin(admin: Admin_update, token: str = Depends(JWTBearer())):
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
    result = Admin_service(db).Admin_updates(email, admin)
    return JSONResponse(status_code=200, content={"mensage": "EL admin ha sido actualizado"})


@admin_router.delete("/dalete/admin", tags=["CRUD ADMIN"], dependencies=[Depends(JWTBearer())])
async def delete_delete(email: str):
    """
    esta funcion eliminar un registro de tipo admin,
    con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
    seguridad ya que los admins tienen varios permisos, luego de valiadar, si el token no es correcto

    retorna un error, pero si si, verifica los datos y sin son validos retornara que el usuario ha sido eliminado
    """
    validate = Admin_service(db).validate_admin(email)
    if not validate:
        return JSONResponse(content={"mensage": "el usuario no tiene permisos"})
    result = Admin_service(db).delete_admin(email=email)
    return JSONResponse(status_code=200, content={"mensage": "el admin ha sido eliminados"})
