from fastapi import APIRouter, HTTPException, status
from utils.jwt_manger import create_token
from services.admin_services import Admin_service
from services.affiliate_services import Affiliate_service
from config.db import Session
from fastapi.responses import JSONResponse

login_router = APIRouter()


@login_router.get("/login", tags=["auth"])
def login(email: str, password: str):
    """
    esta funcion permite  validar el tipo de token, tambien
    puede validar si el token es de tipo usuario o de admin, esto por 
    medio de la libreria de oaut jwt, tambien crea los token
    retorna el token si esta todo bien.

    """
    db = Session()

    validate_affiliate = Affiliate_service(
        db).vericate_afilate(email, password)

    if validate_affiliate:
        validate_affiliate_dict = {
            "id": validate_affiliate.id,
            "email": validate_affiliate.email,
        }

        # Crear el token
        token: str = create_token(validate_affiliate_dict)

        return JSONResponse(status_code=200, content={
            "access_token": token,
            "token_type": "bearer",
            "user_type": "affiliate"
        })
    else:
        db = Session()

    validate_affiliate = Admin_service(
        db).verificate_admin(email, password)

    if validate_affiliate:
        validate_affiliate_dict = {
            "id": validate_affiliate.id,
            "email": validate_affiliate.email,
        }

        token: str = create_token(validate_affiliate_dict)
        return JSONResponse(status_code=200, content={
            "access_token": token,
            "token_type": "bearer",
            "user_type": "admin"
        })

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="El usuario no está registrado"
    )
