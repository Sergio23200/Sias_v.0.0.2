from schemas.affiliate_schema import Affiliate_schema, affilate_update, filter_afiliate_schema, return_afiliate
from services.admin_services import Admin_service
from fastapi.responses import JSONResponse
from config.db import Session
from typing import Optional
from fastapi.encoders import jsonable_encoder
from services.affiliate_services import Affiliate_service
from fastapi import APIRouter, Depends, HTTPException, Query
from utils.jwt_manger import validate_token
from middleware.jwt_bear import JWTBearer
from schemas.affiliate_schema import LoginChatbotRequest
affiliate_router = APIRouter()

db = Session()


@affiliate_router.get("/all/affiliate", tags=["CRUD AFILADOS"])
async def get_all_affiliate():
    """
    esta funcion trear todos los  registro de la base de datos de  afiliado
    con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
    seguridad ya que los afiliados tienen varios permisos, luego de valiadar, si el token no es correcto
    retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
    """
    results = Affiliate_service(db).get_afiliate()
    users = []
    print(results)
    for result in results:
        template = {
            "nombre": result.fullname,
            "cedula": result.document_number,
            "fecha_nacimiento": result.birthdate,
            "tipo_afiliacion": result.membership_type
        }
        users.append(template)
    return JSONResponse(status_code=200, content=jsonable_encoder(users))


@affiliate_router.get("/filter/affiliate", tags=["CRUD AFILADOS"], dependencies=[Depends(JWTBearer())])
async def gat_filter_affiliate(id: Optional[int] = Query(None),
                               document_number: Optional[str] = Query(None),
                               email_f: Optional[str] = Query(None),
                               clinical_historial: Optional[int] = Query(None),
                               city: Optional[int] = Query(None),
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
    filters = filter_afiliate_schema(id=id,
                                     email=email_f,
                                     document_number=document_number,
                                     Clinical_history=clinical_historial,
                                     city=city)

    result = Affiliate_service(db).get_affiliates_filter(filters)

    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@affiliate_router.put("/update/affiliate", tags=["CRUD AFILADOS"], dependencies=[Depends(JWTBearer())])
async def update_afiliate(affialte: affilate_update, token: str = Depends(JWTBearer())):
    """
    esta funcion actualiza un registro de tipo afiliadoutilizando el archivo en el paquete de schema,
    con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
    seguridad ya que los afiliado tienen varios permisos, luego de valiadar, si el token no es correcto
    retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
    """
    payload = validate_token(token)
    id = payload.get("id")
    Affiliate_service(db).Affiliate_update(id, affialte)
    return JSONResponse(status_code=200, content={"mensage": "EL afiliado ha sido actualizado"})


@affiliate_router.delete("/delete/affiliate", tags=["CRUD AFILADOS"])
async def delete_affialte(id: int):
    """
    esta funcion eliminar un registro de tipo admin,
    con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
    seguridad ya que los admins tienen varios permisos, luego de valiadar, si el token no es correcto
    retorna un error, pero si si, verifica los datos y sin son validos retornara que el usuario ha sido eliminado
    """
    if not id:
        raise HTTPException(
            status_code=400, detail="No se pudo obtener el número de documento del token")
    result = Affiliate_service(db).delete_affilate(id)

    return JSONResponse(status_code=200, content={"message": "El afiliado ha sido eliminado"})


@affiliate_router.post("/chatbot/login", tags=["CRUD AFILIADOS CHATBOT"])
async def login_chatbot(request: filter_afiliate_schema):
    result = Affiliate_service(db).get_affiliates_filter(request)

    return result
