from fastapi import APIRouter, Request, Depends, Form
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
from middleware.jwt_bear import JWTBearer
from services.affiliate_services import Affiliate_service
from config.db import Session
from schemas.affiliate_schema import affilate_update
db = Session()
Config_datos_router = APIRouter()

template = Jinja2Templates(directory="frontend")


@Config_datos_router.get("/Config/user", tags=["CONFIGURACION CUENTA USER"], dependencies=[Depends(JWTBearer())])
async def configuracion(request: Request, token: str = Depends(JWTBearer())):
    email = token["email"]
    resultado = Affiliate_service(db).validate_affilate_email(email=email)
    return template.TemplateResponse("templates/configurarCuenta.html", {
        "request": request,
        "id": resultado.id,
        "fullname": resultado.fullname,
        "email": resultado.email,
        "number": resultado.phone_number,
        "city": resultado.city,
        "number_document": resultado.document_number,
        "second_number": resultado.phone_number,
        "type_document": resultado.document_type,
        "membership_type": resultado.membership_type,
        "created_date": resultado.created_date,
        "birthdate": resultado.birthdate
    })


@Config_datos_router.get("/update/userpg", tags=["CONFIGURACION CUENTA USER"], dependencies=[Depends(JWTBearer())])
async def get_update_pg(request: Request, token: str = Depends(JWTBearer())):
    return template.TemplateResponse(
        "templates/actualizarDatosUser.html",
        {"request": request, "token": token}
    )


@Config_datos_router.post("/update/user", tags=["CONFIGURACION CUENTA USER"], dependencies=[Depends(JWTBearer())])
async def get_update_pg(request: Request, email: str = Form(...),
                        Address: str = Form(...),
                        phone_number: int = Form(...),
                        city: str = Form(...),
                        password: str = Form(...),
                        membership_type: str = Form(...),
                        token: str = Depends(JWTBearer())):
    id = token["id"]
    data = affilate_update(city=city, email=email, Address=Address,
                           phone_number=phone_number, password=password, membership_type=membership_type)
    update = Affiliate_service(db).Affiliate_update(data=data, id=id)

    return template.TemplateResponse(
        "templates/paginaPrincipal.html",
        {"request": request, "token": token}
    )


@Config_datos_router.delete("/delete/user", tags=["CONFIGURACION CUENTA USER"], dependencies=[Depends(JWTBearer())])
async def delete_user(request: Request, token: str = Depends(JWTBearer())):
    id = token['id']
    Affiliate_service(db).delete_affilate(id=id)

    return template.TemplateResponse(
        "templates/inicioSesion.html",
        {"request": request, "token": token}
    )
