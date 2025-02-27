from fastapi import APIRouter, HTTPException, status, Form
from fastapi import Request
from fastapi.templating import Jinja2Templates

test_router = APIRouter()
template = Jinja2Templates(directory=("frontend"))


@test_router.get("/test", tags=["auth"])
def login_sesion(request: Request):

    return template.TemplateResponse("templates/listaAfiliados.html", {"request": request})
