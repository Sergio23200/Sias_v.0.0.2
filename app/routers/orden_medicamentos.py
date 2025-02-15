from fastapi import APIRouter
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates

orden_medicamentos_router = APIRouter()

template = Jinja2Templates(directory="frontend")


@orden_medicamentos_router.get("/orden_medicamentos", tags=["orden_medicamentos"])
def orden_medicamentos(request: Request):

    return template.TemplateResponse("templates/ordenMedicamentosUser.html", {"request": request})


@orden_medicamentos_router.post("/agendamiento_citas_confirmacion", tags=["orden_medicamentos"])
def orden_medicamentos_confirmacion(request: Request):
    return template.TemplateResponse("templates/ordenMedicamentosConfirmacion.html", {"request": request})
