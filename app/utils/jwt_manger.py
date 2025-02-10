from jwt import encode, decode
from fastapi import HTTPException


def create_token(data: dict):
    """
    esta funcion permite  validar el tipo de token, tambien
    puede validar si el token es de tipo usuario o de admin, esto por 
    medio de la libreria de oaut jwt, tambien crea los token
    retorna el token si esta todo bien.

    """
    token: str = encode(payload=data, key="my_secret_key", algorithm="HS256")
    return token


def validate_token(token: str) -> dict:
    """
    esta funcion permite  validar el tipo de token, tambien
    puede validar si el token es de tipo usuario o de admin, esto por 
    medio de la libreria de oaut jwt, tambien crea los token
    retorna el token si esta todo bien.

    """
    if not token:
        raise HTTPException(status_code=401, detail="Token is missing.")

    # Eliminar prefijo 'Bearer ' si está presente
    if token.startswith("Bearer "):
        token = token[len("Bearer "):]

    # Decodificar el token
    try:
        data = decode(token, key="my_secret_key", algorithms=["HS256"])
        return data
    except Exception as e:
        raise HTTPException(
            status_code=401, detail=f"Invalid token: {str(e)}")


def decode_token(token: str) -> dict:  # Cambié de 'validate_token' a 'decode_token'
    """
    Decodifica y valida el token JWT.
    """
    if not token:
        raise HTTPException(status_code=401, detail="Token is missing.")

    if token.startswith("Bearer "):
        token = token[len("Bearer "):]

    try:
        data = decode(token, key="my_secret_key", algorithms=["HS256"])
        return data
    except Exception as e:
        raise HTTPException(
            status_code=401, detail=f"Invalid token: {str(e)}")
