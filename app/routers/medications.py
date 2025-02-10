from schemas.Medications_schema_base import Medications_schema, Medications_update, Medications_user, medicatios_filter_schema
from schemas.medications_user_schema import Medications_user_schema
from services.medications_user_services import Medications_user_service
from services.affiliate_services import Affiliate_service
from services.Medications_service import Medications_service
from services.admin_services import Admin_service
from config.db import Session
from utils.jwt_manger import validate_token
from typing import Optional
from fastapi.responses import JSONResponse
from middleware.jwt_bear import JWTBearer
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Depends, Query

medications_router = APIRouter()
db = Session()


@medications_router.get("/all/medications", tags=["CRUD MEDICATIONS"], dependencies=[Depends(JWTBearer())])
async def get_all_medications(token: str = Depends(JWTBearer())):
    """
    esta funcion trear todos los  registro de la base de datos de  medications,
    con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
    seguridad ya que los admins tienen varios permisos, luego de valiadar, si el token no es correcto
    retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
    """
    payload = validate_token(token)
    email = payload.get("email")
    validate = Admin_service(db).validate_admin(email)
    if not validate:
        return JSONResponse(content={"mensage": "el usuario no tiene permisos"})
    result = Medications_service(db).get_medications()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@medications_router.get("/filter/medications", tags=["CRUD MEDICATIONS"], dependencies=[Depends(JWTBearer())])
async def get_filter_medications(id: Optional[int] = Query(None),
                                 generic_name: Optional[str] = Query(None),
                                 price: Optional[str] = Query(None),
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
    filters = medicatios_filter_schema(
        id=id, generic_name=generic_name, price=price)
    result = Medications_service(db).get_medications_filter(valor=filters)
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@medications_router.post("/create/medications", tags=["CRUD MEDICATIONS"], dependencies=[Depends(JWTBearer())])
async def create_medications(medications: Medications_schema, token: str = Depends(JWTBearer())):
    """
    esta funcion crea un registro de tipo medications utilizando el archivo en el paquete de schema,
    con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
    seguridad ya que los afiliados  tienen varios permisos, luego de valiadar, si el token no es correcto
    retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
    """
    payload = validate_token(token)
    email = payload.get("email")
    validate = Admin_service(db).validate_admin(email)
    if not validate:
        return JSONResponse(content={"mensage": "el usuario no tiene permisos"})
    result = Medications_service(db).create_medications(medications)
    return JSONResponse(content={"mensage": "el medicamento se ha registrado"})


@medications_router.post("/user/medications", tags=["CRUD MEDICATIONS"], dependencies=[Depends(JWTBearer())])
async def user_medication(data: Medications_user, generic_name: str, token: str = Depends(JWTBearer())):
    """
    esta funcion actualiza un registro de tipo medications utilizando el archivo en el paquete de schema,
    con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
    seguridad ya que los admins tienen varios permisos, luego de valiadar, si el token no es correcto
    retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
    """
    payload = validate_token(token)

    email = payload.get("email")

    dat = Affiliate_service(db).return_date(email)
    fullname = dat.fullname
    user_medi = Medications_user_schema(
        generic_name=generic_name,
        fullname_user=fullname,
        affiliate=fullname,
        Stocks=data.Stocks
    )
    user = Medications_user_service(db).create_medications_user(user_medi)
    medi = Medications_service(db).user_medications(
        generic_name=generic_name, query=data)
    return medi


@medications_router.put("/update/medications", tags=["CRUD MEDICATIONS"], dependencies=[Depends(JWTBearer())])
async def update_medications(generic_name: str, ips: Medications_update, token: str = Depends(JWTBearer())):
    """
    esta funcion actualiza un registro de tipo medications utilizando el archivo en el paquete de schema,
    con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
    seguridad ya que los admins tienen varios permisos, luego de valiadar, si el token no es correcto
    retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
    """
    payload = validate_token(token)
    email = payload.get("email")
    validate = Admin_service(db).validate_admin(email)
    if not validate:
        return JSONResponse(content={"mensage": "el usuario no tiene permisos"})
    result = Medications_service(db).update_medications(generic_name, ips)
    return JSONResponse(status_code=200, content={"mensage": "el medicamento ha sido actualizado"})


@medications_router.delete("/dalete/medicatioMedications_userns", tags=["CRUD MEDICATIONS"], dependencies=[Depends(JWTBearer())])
async def delete_medications(generic_name: str, token: str = Depends(JWTBearer())):
    """
    esta funcion eliminar un registro de tipo medications,
    con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
    seguridad ya que los admins tienen varios permisos, luego de valiadar, si el token no es correcto
    retorna un error, pero si si, verifica los datos y sin son validos retornara que el usuario ha sido eliminado
    """
    payload = validate_token(token)
    email = payload.get("email")
    validate = Admin_service(db).validate_admin(email)
    if not validate:
        return JSONResponse(content={"mensage": "el usuario no tiene permisos"})
    result = Medications_service(db).delete_medications(generic_name)
    return JSONResponse(status_code=200, content={"mensage": "el medicamento ha sido eliminados"})
