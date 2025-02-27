from fastapi import APIRouter, Request, Depends, Form
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
from middleware.jwt_bear import JWTBearer
from services.admin_services import Admin_service
from schemas.admin_schema import Admin_update
from config.db import Session
db = Session()
Config_datos_router_admin = APIRouter()

template = Jinja2Templates(directory="frontend")


@Config_datos_router_admin.get("/admin/config", tags=["CONFIGURACION CUENTA ADMIN"], dependencies=[Depends(JWTBearer())])
async def configuracion(request: Request, token: str = Depends(JWTBearer())):
    email = token["email"]
    resultado = Admin_service(db).validate_admin(email=email)
    return template.TemplateResponse("templates/configurarCuentaAdmin.html", {
        "request": request,
        "id": resultado.id,
        "fullname": resultado.fullname,
        "email": resultado.email,
        "number": resultado.first_number,
        "city": resultado.city,
        "number_document": resultado.document_number,
        "type_document": resultado.document_type,
        "first_number": resultado.first_number,
        "job_title": resultado.job_title,
        "birthdate": resultado.birthdate
    })


@Config_datos_router_admin.get("/update/adminpg", tags=["CONFIGURACION CUENTA ADMIN"], dependencies=[Depends(JWTBearer())])
async def get_update_pg(request: Request, token: str = Depends(JWTBearer())):
    return template.TemplateResponse(
        "templates/actualizarDatosAdmin.html",
        {"request": request, "token": token}
    )


@Config_datos_router_admin.delete("/delete/user", tags=["CONFIGURACION CUENTA ADMIN"], dependencies=[Depends(JWTBearer())])
async def delete_user(request: Request, token: str = Depends(JWTBearer())):
    email = token['email']
    Admin_service(db).delete_admin(email=email)

    return template.TemplateResponse(
        "templates/inicioSesion.html",
        {"request": request, "token": token}
    )


@Config_datos_router_admin.post("/update/admin", tags=["CONFIGURACION CUENTA ADMIN"], dependencies=[Depends(JWTBearer())])
async def get_update_pg(request: Request, email: str = Form(...),
                        first_number: str = Form(...),
                        city: str = Form(...),
                        password: str = Form(...),
                        job_title: str = Form(...),
                        token: str = Depends(JWTBearer())):
    email = token["email"]
    data = Admin_update(city=city, email=email,
                        first_number=first_number, password=password, job_title=job_title)
    update = Admin_service(db).Admin_updates(data=data, email=email)

    return template.TemplateResponse(
        "templates/paginaPrincipalAdministrador.html",
        {"request": request, "token": token}
    )
