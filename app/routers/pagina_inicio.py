from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from middleware.jwt_bear import JWTBearer
from services.admin_services import Admin_service
from config.db import Session

db = Session()

pagina_inicio_router = APIRouter()
template = Jinja2Templates(directory="frontend")


@pagina_inicio_router.get("/inicio", tags=["pagina_principal"], dependencies=[Depends(JWTBearer())])
def pagina_principal(request: Request, token: str = Depends(JWTBearer())):
    return template.TemplateResponse(
        "templates/paginaPrincipal.html",
        {"request": request, "token": token}
    )


@pagina_inicio_router.get("/inicio_admin", tags=["pagina_principal"], dependencies=[Depends(JWTBearer())])
def pagina_principal_admin(request: Request,  token: str = Depends(JWTBearer())):
    email = token["email"]
    print(f'este es el email{email}')
    resultado = Admin_service(db).validate_admin(email=email)
    print(f'este es el resultado{resultado}')
    return template.TemplateResponse("templates/paginaPrincipalAdministrador.html", {
        "request": request,
        "fullname": resultado.fullname,
        "email": email,
        "job_title": resultado.job_title
    })
