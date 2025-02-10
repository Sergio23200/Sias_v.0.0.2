from fastapi import APIRouter, HTTPException, status, Form
from fastapi import Request
from fastapi.templating import Jinja2Templates

registro_router = APIRouter()
template = Jinja2Templates(directory=("frontend"))


@registro_router.get("/registro", tags=["auth"])
def registro(request: Request):
    return template.TemplateResponse("templates/registro.html", {"request": request})
