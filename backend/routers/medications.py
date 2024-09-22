from schemas.Medications_schema import Medications_schema, Medications_update
from config.db import Session
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from services.Medications_service import Medications_service
from fastapi import APIRouter

medications_router = APIRouter()


@medications_router.post("/create/medications", tags=["CRUD MEDICATIONS"])
async def create_medications(medications: Medications_schema):
    db = Session()
    result = Medications_service(db).create_medications(medications)
    return JSONResponse(content={"mensage": "el medicamento se ha registrado"})


@medications_router.get("/all/medications", tags=["CRUD MEDICATIONS"])
async def get_all_medications():
    db = Session()
    result = Medications_service(db).get_medications()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@medications_router.put("/update/medications", tags=["CRUD MEDICATIONS"])
async def update_medications(generic_name: str, ips: Medications_update):
    db = Session()
    result = Medications_service(db).update_medications(generic_name, ips)
    return JSONResponse(status_code=200, content={"mensage": "el medicamento ha sido actualizado"})


@medications_router.delete("/dalete/medications", tags=["CRUD MEDICATIONS"])
async def delete_medications(generic_name: str):
    db = Session()
    result = Medications_service(db).delete_medications(generic_name)
    return JSONResponse(status_code=200, content={"mensage": "el medicamento ha sido eliminados"})
