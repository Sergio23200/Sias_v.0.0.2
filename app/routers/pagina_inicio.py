from fastapi import APIRouter, HTTPException, status, Form, Request, Depends
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from utils.jwt_manger import create_token
from services.admin_services import Admin_service
from middleware.jwt_bear import JWTBearer
from services.affiliate_services import Affiliate_service
from config.db import Session
from schemas.login_schema import login_schema_sign_up

pagina_inicio_router = APIRouter()
template = Jinja2Templates(directory="frontend")


@pagina_inicio_router.get("/inicio", tags=["pagina_principal"], dependencies=[Depends(JWTBearer())])
def pagina_principal(request: Request, token: str = Depends(JWTBearer())):
    return template.TemplateResponse(
        "templates/paginaPrincipal.html",
        {"request": request, "token": token}
    )


@pagina_inicio_router.get("/inicio_admin", tags=["pagina_principal"], dependencies=[Depends(JWTBearer())])
def pagina_principal_admin(request: Request):
    return template.TemplateResponse("templates/paginaPrincipalAdministrador.html", {"request": request})
