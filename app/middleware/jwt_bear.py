from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from utils.jwt_manger import validate_token
from config.db import Session
from models.Admin import Admin_model
from fastapi import Request, HTTPException
from sqlalchemy.orm.exc import NoResultFound

"""
en este modulo validamos el token
que recibimos del usuarios
"""


class JWTBearer(HTTPBearer):
    """
    se recibe el token, luego de eso por medio 
    de fastapi.security, dependiendo si las credenciales son validas
    las retornara, sino devolvera un httpexception, diciendo que el token
    es invalido.

    """

    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request) -> str:
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)

        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(
                    status_code=403, detail="Invalid authentication scheme.")
            return credentials.credentials
        else:
            raise HTTPException(
                status_code=403, detail="Invalid authorization code.")
