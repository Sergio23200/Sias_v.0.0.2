from fastapi import FastAPI, Request, Depends, HTTPException, status, Form
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import CRUD
import models

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


@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user = CD.authenticate_affiliate(form.username, form.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="El usuario no se ha encontrado")

    return {"session_token": user.document_number, "token_type": "bearer"}


@app.get("/information/me")
async def information(token: int = Depends(current_user)):
    return token


@app.delete("/user/delete")
async def user_delete(token: int = Depends(current_user)):
    token = token["document_number"]
    user_drop = CD.delete_affiliate(token)
    if not user_drop:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El proceso no se puede completar"
        )
    return {"detail": "El usuario ha sido eliminado"}


@app.post("/user/create")
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
