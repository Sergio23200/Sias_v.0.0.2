from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from middleware.jwt_bear import JWTBearer
from services.admin_services import Admin_service
from config.db import Session

db = Session()

gestion_admin_router = APIRouter()
template = Jinja2Templates(directory="frontend")


@gestion_admin_router.get("/gestion/user", tags=["pagina_principal"], dependencies=[Depends(JWTBearer())])
def pagina_principal(request: Request, token: str = Depends(JWTBearer())):

    return template.TemplateResponse("templates/listaAfiliados.html", {"request": request})
