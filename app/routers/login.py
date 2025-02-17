from fastapi import APIRouter, HTTPException, status, Form, Request
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from utils.jwt_manger import create_token
from services.admin_services import Admin_service
from services.affiliate_services import Affiliate_service
from config.db import Session
from schemas.login_schema import login_schema_sign_up

login_router = APIRouter()
template = Jinja2Templates(directory="frontend")


@login_router.get("/", tags=["auth"])
def login_sesion(request: Request):
    return template.TemplateResponse("templates/inicioSesion.html", {"request": request})


@login_router.post("/login/", tags=["auth"])
def login(document_type: str = Form(...),
          document_number: str = Form(...),
          password: str = Form(...)):
    """
    Valida las credenciales del usuario, genera un token JWT y redirige a la página principal.
    El token se almacena en una cookie HTTPOnly por seguridad.
    """
    login_schema = login_schema_sign_up(document_type=document_type,
                                        document_number=document_number,
                                        password=password)
    db = Session()

    validate_user = Affiliate_service(db).vericate_afilate(
        login_schema_sign_up=login_schema)
    user_type = "affiliate" if validate_user else None

    if not validate_user:
        validate_user = Admin_service(db).verificate_admin(
            login_schema_sign_up=login_schema)
        user_type = "admin" if validate_user else None

    if validate_user:
        user_data = {"id": validate_user.id, "email": validate_user.email}
        token: str = create_token(user_data)

        if user_type == "affiliate":
            response = RedirectResponse(url="/inicio", status_code=302)
        else:
            response = RedirectResponse(url="/inicio_admin", status_code=302)

        response.set_cookie(key="access_token", value=token,
                            httponly=True, secure=True, samesite="Lax")

        return response

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="El usuario no está registrado"
    )
