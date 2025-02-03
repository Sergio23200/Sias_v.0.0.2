from fastapi import APIRouter, HTTPException, status, Form, Depends, Body
from utils.jwt_manger import create_token
from services.admin_services import Admin_service
from services.affiliate_services import Affiliate_service
from config.db import Session
from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from schemas.login_schema import login_schema_sign_up

from middleware.jwt_bear import JWTBearer

login_router = APIRouter()
template = Jinja2Templates(directory=("frontend"))


@ login_router.get("/", tags=["auth"])
def login_sesion(request: Request):
    return template.TemplateResponse("templates/inicio_sesion.html", {"request": request})


@login_router.get("/inicio", tags=["pagina_principal"], dependencies=[Depends(JWTBearer())])
def pagina_principal(request: Request):
    return template.TemplateResponse("templates/pagina_principal.html", {"request": request})


@login_router.post("/login/", tags=["auth"], )
def login(login_schema: login_schema_sign_up = Body(...)):
    """
    esta funcion permite  validar el tipo de token, tambien
    puede validar si el token es de tipo usuario o de admin, esto por
    medio de la libreria de oaut jwt, tambien crea los token
    retorna el token si esta todo bien.


    """
    db = Session()
    validate_affiliate = Affiliate_service(
        db).vericate_afilate(login_schema_sign_up=login_schema)
    if validate_affiliate:
        validate_affiliate_dict = {
            "id": validate_affiliate.id,
            "email": validate_affiliate.email,
        }

        token: str = create_token(validate_affiliate_dict)

        return JSONResponse(status_code=200, content={
            "access_token": token,
            "token_type": "bearer",
            "user_type": "affiliate"
        })
    else:
        db = Session()

    validate_affiliate = Admin_service(
        db).verificate_admin(login_schema_sign_up=login_schema)

    if validate_affiliate:
        validate_affiliate_dict = {
            "id": validate_affiliate.id,
            "email": validate_affiliate.email,
        }

        token: str = create_token(validate_affiliate_dict)
        return JSONResponse(status_code=200, content={
            "access_token": token,
            "token_type": "bearer",
            "user_type": "admin"
        })

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="El usuario no está registrado"
    )
