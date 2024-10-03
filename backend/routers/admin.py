from schemas.admin_schema import Admin_schema, Admin_update
from services.admin_services import Admin_service
from config.db import Session
from middleware.jwt_bear import JWTBearer, validate_token
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Depends

admin_router = APIRouter()


@admin_router.post("/create/admin", tags=["CRUD ADMIN"], dependencies=[Depends(JWTBearer())])
async def create_admin(affiliate: Admin_schema, token: str = Depends(JWTBearer())):
    """
    esta funcion crea un registro de tipo admin utilizando el archivo en el paquete de schema,
    con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
    seguridad ya que los admins tienen varios permisos, luego de valiadar, si el token no es correcto
    retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
    """
    payload = validate_token(token)
    email = payload.get("email")
    validate = Admin_service(db).validate_admin(email)
    if not validate:
        return JSONResponse(content={"mensage": "el usuario no tiene permisos"})
    db = Session()
    Admin_service(db).create_Admin(affiliate)
    return JSONResponse(content={"mensage": "el usuario se ha registrado"})


@admin_router.get("/all/admin", tags=["CRUD ADMIN"], dependencies=[Depends(JWTBearer())])
async def get_all_admin(token: str = Depends(JWTBearer())):
    """
    esta funcion trear todos los  registro de la base de datos de  admin,
    con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
    seguridad ya que los admins tienen varios permisos, luego de valiadar, si el token no es correcto
    retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
    """
    payload = validate_token(token)
    db = Session()
    email = payload.get("email")
    validate = Admin_service(db).validate_admin(email)
    if not validate:
        return JSONResponse(content={"mensage": "el usuario no tiene permisos"})

    result = Admin_service(db).get_admin()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@admin_router.put("/update/admin", tags=["CRUD ADMIN"])
async def update_admin(document_number: int, admin: Admin_update):
    """
    esta funcion actualiza un registro de tipo admin utilizando el archivo en el paquete de schema,
    con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
    seguridad ya que los admins tienen varios permisos, luego de valiadar, si el token no es correcto
    retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
    """
    db = Session()
    result = Admin_service(db).Admin_updates(document_number, admin)
    return JSONResponse(status_code=200, content={"mensage": "EL admin ha sido actualizado"})


@admin_router.delete("/dalete/admin", tags=["CRUD ADMIN"], dependencies=[Depends(JWTBearer())])
async def delete_delete(document_number: int):
    """
    esta funcion eliminar un registro de tipo admin,
    con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
    seguridad ya que los admins tienen varios permisos, luego de valiadar, si el token no es correcto
    retorna un error, pero si si, verifica los datos y sin son validos retornara que el usuario ha sido eliminado
    """
    db = Session()
    result = Admin_service(db).delete_admin(document_number)
    return JSONResponse(status_code=200, content={"mensage": "el admin ha sido eliminados"})
