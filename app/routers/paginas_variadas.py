from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from middleware.jwt_bear import JWTBearer

paginas_variadas_router = APIRouter()
template = Jinja2Templates(directory="frontend")


@paginas_variadas_router.get("/inicio/politicas_privacidad", tags=["PAGINAS VARIADAS"], dependencies=[Depends(JWTBearer())])
async def get_politca_privacidad(request: Request):
    return template.TemplateResponse("templates/politicasPrivacidad.html", {"request": request})


@paginas_variadas_router.get("/inicio/noticias", tags=["PAGINAS VARIADAS"], dependencies=[Depends(JWTBearer())])
async def get_pagina_noticias(request: Request):
    return template.TemplateResponse("templates/paginaNoticias.html", {"request": request})


@paginas_variadas_router.get("/inicio/terminos_condiciones", tags=["PAGINAS VARIADAS"], dependencies=[Depends(JWTBearer())])
async def get_terminos_condiciones(request: Request):
    return template.TemplateResponse("templates/terminosCondiciones.html", {"request": request})


@paginas_variadas_router.get("/inicio/redes_sociales", tags=["PAGINAS VARIADAS"], dependencies=[Depends(JWTBearer())])
async def get_redes_sociales(request: Request):
    return template.TemplateResponse("templates/mediosDeContacto.html", {"request": request})
