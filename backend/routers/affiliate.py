from schemas.affiliate_schema import Affiliate_schema, affilate_update
from fastapi.responses import JSONResponse
from routers.login import token_user
from config.db import Session
from fastapi.encoders import jsonable_encoder
from services.affiliate_services import Affiliate_service
from fastapi import APIRouter, Depends, HTTPException
from middleware.jwt_bear import JWTBearer, validate_token
affiliate_router = APIRouter()

tokens = token_user


@affiliate_router.post("/create/affiliate", tags=["CRUD AFILADOS"])
async def create_affiliate(affiliate: Affiliate_schema):
    """
    esta funcion crea un registro de tipo afiliado utilizando el archivo en el paquete de schema,
    con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
    seguridad ya que los afiliados  tienen varios permisos, luego de valiadar, si el token no es correcto
    retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
    """
    db = Session()
    Affiliate_service(db).create_Affiliate(affiliate)
    return JSONResponse(content={"mensage": "el usuario se ha registrado"})


@affiliate_router.get("/all/affiliate", tags=["CRUD AFILADOS"], dependencies=[Depends(JWTBearer())])
async def get_all_affiliate():
    """
    esta funcion trear todos los  registro de la base de datos de  afiliado
    con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
    seguridad ya que los afiliados tienen varios permisos, luego de valiadar, si el token no es correcto
    retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
    """
    db = Session()
    result = Affiliate_service(db).get_afiliate()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@affiliate_router.get("/filter/affiliate", tags=["CRUD AFILADOS"], dependencies=[Depends(JWTBearer())])
async def gat_filter_affiliate(token: str = Depends(JWTBearer())):
    """
    esta funcion trear todos los  registro de la base de datos de  afiliado
    con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
    seguridad ya que los afiliados tienen varios permisos, luego de valiadar, si el token no es correcto
    retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
    """
    db = Session()
    payload = validate_token(token)
    id = payload.get("id")

    if not id:
        raise HTTPException(
            status_code=400, detail="Invalid token or ID not found.")

        # Lógica del servicio de afiliados
    result = Affiliate_service(db).get_affiliates_filter(id)

    # Devolver el resultado
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
    db = Session()
    Affiliate_service(db).Affiliate_update(id, affialte)
    return JSONResponse(status_code=200, content={"mensage": "EL afiliado ha sido actualizado"})


@affiliate_router.delete("/delete/affiliate", tags=["CRUD AFILADOS"], dependencies=[Depends(JWTBearer())])
async def delete_affialte(token: str = Depends(JWTBearer())):
    """
    esta funcion eliminar un registro de tipo admin,
    con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
    seguridad ya que los admins tienen varios permisos, luego de valiadar, si el token no es correcto
    retorna un error, pero si si, verifica los datos y sin son validos retornara que el usuario ha sido eliminado
    """
    payload = validate_token(token)
    id = payload.get("id")
    if not id:
        raise HTTPException(
            status_code=400, detail="No se pudo obtener el número de documento del token")
    db = Session()
    result = Affiliate_service(db).delete_affilate(id)

    return JSONResponse(status_code=200, content={"message": "El afiliado ha sido eliminado"})
