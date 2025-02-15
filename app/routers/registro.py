from fastapi import APIRouter, HTTPException, status, Form
from fastapi import Request
from fastapi.templating import Jinja2Templates
from schemas.affiliate_schema import Affiliate_schema
from services.affiliate_services import Affiliate_service
from fastapi.responses import JSONResponse
from config.db import Session
from fastapi.responses import RedirectResponse
from datetime import date
db = Session()

registro_router = APIRouter()
template = Jinja2Templates(directory=("frontend"))


@registro_router.get("/registro", tags=["auth"])
def registro(request: Request):
    return template.TemplateResponse("templates/registro.html", {"request": request})


@registro_router.post("/create/affiliate", tags=["CRUD AFILADOS"])
async def create_affiliate(
        fullname: str = Form(...),
        document_type: str = Form(...),
        document_number: int = Form(...),
        birthdate: date = Form(...),
        gender: str = Form(...),
        email: str = Form(...),
        Address: str = Form(...),
        Clinical_history: int = Form(...),
        phone_number: int = Form(...),
        city: str = Form(...),
        password: str = Form(...),
        membership_type: str = Form(...)):
    """
    esta funcion crea un registro de tipo afiliado utilizando el archivo en el paquete de schema,

    con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
    seguridad ya que los afiliados  tienen varios permisos, luego de valiadar, si el token no es correcto
    retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
    """
    affiliate = Affiliate_schema(
        fullname=fullname,
        document_type=document_type,
        document_number=document_number,
        birthdate=birthdate,
        gender=gender,
        email=email,
        Address=Address,
        Clinical_history=Clinical_history,
        phone_number=phone_number,
        city=city,
        password=password,
        membership_type=membership_type
    )
    Affiliate_service(db).create_Affiliate(affiliate)
    return RedirectResponse(url="/noti", status_code=302)


@registro_router.get("/noti", tags=["auth"])
def noti(request: Request):
    return template.TemplateResponse("templates/templateNoti.html", {"request": request})
