from schemas.hospital_chema import Hospital_schema, Hospital_update
from config.db import Session
from middleware.jwt_bear import JWTBearer
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from services.hospital_service import hospìtal_service
from fastapi import APIRouter, Depends

hospital_router = APIRouter()


@hospital_router.post("/create/hospital", tags=["CRUD HOSPITAL"], dependencies=[Depends(JWTBearer())])
async def create_hospital(hospital: Hospital_schema):
    db = Session()
    hospìtal_service(db).create_hospital(hospital)
    return JSONResponse(content={"mensage": "el hospital se ha registrado"})


@hospital_router.get("/all/hospital", tags=["CRUD HOSPITAL"], dependencies=[Depends(JWTBearer())])
async def get_all_hospital():
    db = Session()
    result = hospìtal_service(db).get_hospital()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@hospital_router.put("/update/hospital", tags=["CRUD HOSPITAL"], dependencies=[Depends(JWTBearer())])
async def update_hospital(name_hospital: int, hospital: Hospital_update):
    db = Session()
    result = hospìtal_service(db).update_hospital(name_hospital, hospital)
    return JSONResponse(status_code=200, content={"mensage": "EL hospital ha sido actualizado"})


@hospital_router.delete("/dalete/hospital", tags=["CRUD HOSPITAL"], dependencies=[Depends(JWTBearer())])
async def delete_hospital(name_hospital: str):
    db = Session()
    result = hospìtal_service(db).delete_hospital(name_hospital)
    return JSONResponse(status_code=200, content={"mensage": "el hospital ha sido eliminados"})
