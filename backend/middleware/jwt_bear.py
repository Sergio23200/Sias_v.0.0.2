from fastapi.security import HTTPBearer
from utils.jwt_manger import validate_token
from models.Affilate import Affiliate_model
from config.db import Session
from services.affiliate_services import Affiliate_service
from models.Admin import Admin_model
from fastapi import Request, HTTPException
from sqlalchemy.orm.exc import NoResultFound


class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)

        try:
            db = Session()
            validate = Affiliate_service(
                db).validate_affilate(email=data["email"])
        except NoResultFound:
            try:
                validate = Admin_model.get(Admin_model.email == data["email"])
            except NoResultFound:
                raise HTTPException(
                    status_code=403, detail="Credenciales inválidas"
                )

        return validate
