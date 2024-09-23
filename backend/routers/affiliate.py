from schemas.affiliate_schema import Affiliate_schema, affilate_update
from fastapi.responses import JSONResponse
from config.db import Session
from fastapi.encoders import jsonable_encoder
from services.affiliate_services import Affiliate_service
from fastapi import APIRouter, Depends
from middleware.jwt_bear import JWTBearer

affiliate_router = APIRouter()


@affiliate_router.post("/create/affiliate", tags=["CRUD AFILADOS"])
async def create_affiliate(affiliate: Affiliate_schema):
    db = Session()
    Affiliate_service(db).create_Affiliate(affiliate)
    return JSONResponse(content={"mensage": "el usuario se ha registrado"})


@affiliate_router.get("/all/affiliate", tags=["CRUD AFILADOS"], dependencies=[Depends(JWTBearer())])
async def get_all_affiliate():
    db = Session()
    result = Affiliate_service(db).get_afiliate()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@affiliate_router.get("/filter/affiliate", tags=["CRUD AFILADOS"], dependencies=[Depends(JWTBearer())])
async def gat_filter_affiliate(document_number: int):
    db = Session()
    result = Affiliate_service(db).get_affiliates_filter(document_number)
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@affiliate_router.put("/update/affiliate", tags=["CRUD AFILADOS"], dependencies=[Depends(JWTBearer())])
async def update_afiliate(document_number: int, affialte: affilate_update):
    db = Session()
    result = Affiliate_service(db).Affiliate_update(document_number, affialte)
    return JSONResponse(status_code=200, content={"mensage": "EL afiliado ha sido actualizado"})


@affiliate_router.delete("/update/affiliate", tags=["CRUD AFILADOS"], dependencies=[Depends(JWTBearer())])
async def delete_affialte(document_number: int):
    db = Session()
    result = Affiliate_service(db).delete_affilate(document_number)
    return JSONResponse(status_code=200, content={"mensage": "el afiliado ha sido eliminados"})
