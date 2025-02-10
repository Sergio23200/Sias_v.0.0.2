from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer
# Asegúrate de tener la función para decodificar el token
from utils.jwt_manger import decode_token


class JWTBearer(HTTPBearer):
    """
    Middleware que obtiene el token desde las cookies y lo valida.
    """

    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request) -> dict:
        token = request.cookies.get("access_token")  # Leer token desde cookies

        if not token:
            raise HTTPException(status_code=403, detail="No autenticado")

        # Decodificar token
        # Implementa esta función en `jwt_manger`
        payload = decode_token(token)

        if not payload:
            raise HTTPException(
                status_code=403, detail="Token inválido o expirado")

        return payload  # Devuelve la información del usuario
