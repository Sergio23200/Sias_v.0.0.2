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
    db = Session()
    result = specialist_service(db).create_specialist(specialist)
    return JSONResponse(content={"mensage": "el especialista se ha registrado"})


@specialist_router.get("/all/specialist", tags=["CRUD SPECIALIST"], dependencies=[Depends(JWTBearer())])
async def get_all_specialist():
    db = Session()
    result = specialist_service(db).get_specialist()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@specialist_router.put("/update/specialist", tags=["CRUD SPECIALIST"], dependencies=[Depends(JWTBearer())])
async def update_specialist(document_number: int, ips: Specialist_update):
    db = Session()
    result = specialist_service(db).update_specialist(document_number, ips)
    return JSONResponse(status_code=200, content={"mensage": "el especialista ha sido actualizado"})


@specialist_router.delete("/dalete/specialist", tags=["CRUD SPECIALIST"], dependencies=[Depends(JWTBearer())])
async def delete_specialist(document_number: int):
    db = Session()
    result = specialist_service(db).delete_specialist(document_number)
    return JSONResponse(status_code=200, content={"mensage": "el especialista ha sido eliminados"})
