from fastapi import FastAPI, Request, Depends, HTTPException, status, Form
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import CRUD
import models
from typing import Optional
app = FastAPI()

# Definiciones y configuración
DB = models
CD = CRUD
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


async def current_user(token: int = Depends(oauth2_scheme)):
    user = CD.token_oaut(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="El usuario no está autenticado"
        )
    return user


@app.post("/login", tags=["autenticate"])
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user = CD.authenticate_affiliate(form.username, form.password)
    if not user:
        user = CD.authenticete_admin(form.username, form.password)
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="El usuario no se ha encontrado")
        return {"admin_token": user.document_number, "token_type": "bearer"}
    return {"affilite_token": user.document_number, "token_type": "bearer"}


@app.get("/information/me", tags=["autenticate"])
async def information(token: int = Depends(current_user)):
    return token

# affiliate


@app.delete("/user/delete", tags=["CRUD Affiliate"])
async def user_delete(token: int = Depends(current_user)):
    token = token["document_number"]
    user_drop = CD.delete_affiliate(token)
    if not user_drop:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El proceso no se puede completar"
        )
    return {"detail": "El usuario ha sido eliminado"}


@app.post("/user/create", tags=["CRUD Affiliate"])
async def create_user(
    fullname: str = Form(...),
    document_type: str = Form(...),
    document_number: str = Form(...),
    birthdate: str = Form(...),
    email: str = Form(...),
    first_number: str = Form(...),
    second_number: str = Form(...),
    city: str = Form(...),
    password: str = Form(...),
    membership_type: str = Form(...)
):
    try:
        new_user = CRUD.create_affiliates(
            fullname, document_type, document_number,
            birthdate, email, first_number, second_number,
            city, password, membership_type
        )

        if not new_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Error al crear el usuario")

        return {"detail": "El usuario se ha creado con éxito"}

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@app.put("/user/update", tags=["CRUD Affiliate"])
async def affiliate_update(
    token: int = Depends(oauth2_scheme),
    email: str = Form(...),
    first_number: str = Form(...),
    second_number: str = Form(...),
    city: str = Form(...),
    password: Optional[str] = Form(None)
):
    update_affiliate = CD.update_affiliate(
        token, email, first_number, second_number, city, password)
    if not update_affiliate:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="el usuario no se pudo actualizar"
        )

    return update_affiliate
