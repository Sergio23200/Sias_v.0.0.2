from fastapi import APIRouter, HTTPException, status, Form
from fastapi import Request
from fastapi.templating import Jinja2Templates

test_router = APIRouter()
template = Jinja2Templates(directory=("frontend"))


@test_router.get("/test", tags=["auth"])
def login_sesion(request: Request):

<<<<<<< HEAD
    return template.TemplateResponse("templates/actualizarDatosUser.html", {"request": request})
=======
    return template.TemplateResponse("templates/inicio_sesion.html", {"request": request})
>>>>>>> caro_main
