from fastapi import APIRouter, HTTPException, status
from utils.jwt_manger import create_token
from services.affiliate_services import Affiliate_service
from config.db import Session
from fastapi.responses import JSONResponse

login_router = APIRouter()


@login_router.get("/login", tags=["auth"])
def login(email: str, password: str):
    db = Session()

    validate_affiliate = Affiliate_service(
        db).vericate_afilate(email, password)

    if validate_affiliate:
        # Extraemos solo los datos necesarios, evitando atributos no serializables
        validate_affiliate_dict = {
            "id": validate_affiliate.id,
            "email": validate_affiliate.email,
            # otros campos que sean necesarios
        }

        # Crear el token
        token: str = create_token(validate_affiliate_dict)

        return JSONResponse(status_code=200, content={
            "access_token": token,
            "token_type": "bearer",
            "user_type": "affiliate"
        })

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="El usuario no está registrado"
    )
