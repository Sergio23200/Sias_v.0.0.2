from schemas.admin_schema import Admin_schema, Admin_update
from services.admin_services import Admin_service
from config.db import Session
from middleware.jwt_bear import JWTBearer
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Depends

admin_router = APIRouter()


@admin_router.post("/create/admin", tags=["CRUD ADMIN"])
async def create_admin(affiliate: Admin_schema):
    db = Session()
    Admin_service(db).create_Admin(affiliate)
    return JSONResponse(content={"mensage": "el usuario se ha registrado"})


@admin_router.get("/all/admin", tags=["CRUD ADMIN"])
async def get_all_admin():
    db = Session()
    result = Admin_service(db).get_admin()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@admin_router.put("/update/admin", tags=["CRUD ADMIN"])
async def update_admin(document_number: int, admin: Admin_update):
    db = Session()
    result = Admin_service(db).Admin_updates(document_number, admin)
    return JSONResponse(status_code=200, content={"mensage": "EL admin ha sido actualizado"})


@admin_router.delete("/dalete/admin", tags=["CRUD ADMIN"])
async def delete_delete(document_number: int):
    db = Session()
    result = Admin_service(db).delete_admin(document_number)
    return JSONResponse(status_code=200, content={"mensage": "el admin ha sido eliminados"})
