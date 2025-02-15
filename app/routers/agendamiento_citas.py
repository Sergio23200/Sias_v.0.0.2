from fastapi import APIRouter
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates


agendamiento_citas_router = APIRouter()

template = Jinja2Templates(directory="frontend")


@agendamiento_citas_router.get("/agendamiento_citas", tags=["agendamiento_citas"])
def agendamiento_citas(request: Request):

    return template.TemplateResponse("templates/agendamientoCitas.html", {"request": request})
