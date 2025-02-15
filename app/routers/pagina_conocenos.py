from fastapi import APIRouter, Depends
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
from middleware.jwt_bear import JWTBearer

pagina_conocenos_router = APIRouter()

template = Jinja2Templates(directory="frontend")


@pagina_conocenos_router.get("/conocenos", tags=["pagina_conocenos"], dependencies=[Depends(JWTBearer())])
def pagina_conocenos(request: Request):
    return template.TemplateResponse("templates/paginaConocenos.html", {"request": request})
