from fastapi import FastAPI, Request, Depends, HTTPException, status, Form
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import CRUD
import models
from typing import Optional
app = FastAPI()


# post = mandar datos
# put = actualizar datos
# delete = eliminar datos
# get = recibir datos

# Definiciones y configuración
DB = models
CD = CRUD
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


async def current_user(token: int = Depends(oauth2_scheme)):
    """
    declaracion de funcion para la validacion de token actual:

    esta funcion permite por medio de la recoleccion del token validarlo por medio de una funcion importada 
    en el modulo CRUD

    Agrs:
        token : int = depens(ouath2_schema)

    returns:
        dic: un diccionario con los datos del usuario sin la contraseña de usuarior

    Raise:
        HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="El usuario no está autenticado")
    """
    user = CD.token_oaut(token)

    if not user:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="El usuario no está autenticado"
        )
    return user


@app.post("/login", tags=["autenticate"])
async def login(form: OAuth2PasswordRequestForm = Depends()):
    """
    creacion de endpoint para la autenticacion:

    por medio de las variables enviadas por medio de los formularios, por medio de la funcion importada en el modulo CRUD
    con el verificamos si el usuario se esta autenticando como afiliado , como administrador o si no esta en ninguno:

    Agrs:
        (form: OAuth2PasswordRequestForm = Depends())

    returns:
        retorno de diccionario con los datos sin contraseña de afiliados o administradores
    Raise:
        HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="El usuario no se ha encontrado")
    """
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
    """creacion de endpoint para el retorno de la informacion:
    por medio de la dependencia de que creamos con la funcion current_user"""
    return token

# affiliate


@app.delete("/user/delete", tags=["CRUD Affiliate"])
async def user_delete(token: int = Depends(current_user())):

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

# admin


@app.delete("/admin/delete_medicacion", tags=["funcions admin"])
async def admin_delete_medicamentos(generic_name: str, token: int = Depends(current_user())):
    token = token["document_number"]
    query = CD.delete_m(token, generic_name)
    return query


@app.put("/admin/delete_medicacion", tags=["funcions admin"])
async def admin_delete_medicamentos(generic_name: str, dose: int, price: int, contraindications: str, token: int = Depends(current_user())):
    token = token["document_number"]
    query = CD.update_m(token, generic_name, dose, price, contraindications)
    return query


@app.post("/admin/delete_medicacion", tags=["funcions admin"])
async def admin_delete_medicamentos(generic_name: str, dose: int, price: int, contraindications: str, token: int = Depends(current_user())):
    token = token["document_number"]
    query = CD.create_m(token, generic_name, dose, price, contraindications)
    return query


@app.get("/admin/delete_medicacion", tags=["funcions admin"])
async def admin_delete_medicamentos(generic_name: str, token: int = Depends(current_user())):
    token = token["document_number"]
    query = CD.delete_m(generic_name)
    return query

# admin hospitales . 
@app.post("/admin/send_data_hospital", tags=["funtions admin"])
async def admin_send_data_hospital(fullname: str, city_id: str,  Address: str, specialty: str, email: str, phone_number: int, ambulance: int, token: int = Depends(current_user())):
    token = token["document_number"]
    hospital_query = CD.create_hospital(token, fullname, city_id, Address, specialty, email, phone_number, ambulance )
    if not hospital_query:
        raise HTTPException(status,code=status.HTTP_409_CONFLICT, detail="No ha sido posible realizar proceso solicitado , intente nuevamente ")
    return hospital_query

@app.get("/admin/receive_data_hospital", tags=["funtions admin"])
async def admin_receive_data_hospital( fullname: str, token: int = Depends(current_user())):
    token = token["document_number"]
    hospital_query = CD.receive_hospital(fullname)
    if not hospital_query:
        raise HTTPException(status,code=status.HTTP_400_BAD_REQUEST, detail="No ha sido posible realizar proceso solicitado , intente nuevamente ")
    return hospital_query

@app.put("/admin/update_data_hospital", tags=["funtions admin"])
async def admin_update_data_hospital(fullname: str, token: int = Depends(current_user())):
    token = token["document_number"]
    hospital_query = CD.update_hospital(token, fullname)
    if not hospital_query:
        raise HTTPException(status,code=status.HTTP_404_NOT_FOUND, detail="No ha sido posible realizar el proceso de actualizacion , intente nuevamente ")
    return hospital_query

@app.delete("/admin/delete_data_hospital", tags=["funtions admin"])
async def admin_delete_data_hospital(fullname: str, token: int = Depends(current_user())):
    token = token["document_number"]
    hospital_query = CD.delete_hospital(token, fullname)
    if not hospital_query:
        raise HTTPException(status,code=status.HTTP_400_BAD_REQUEST, detail="No ha sido posible eliminar registro indicado , por favor intentelo nuevamente ")
    return hospital_query


# admin centros medicos . 

@app.post("/admin/send_health_center", tags=["funtions admin"])
async def admin_send_health_center(fullname: str, city_id: str,  Address: str, specialty: str, email: str, phone_number: int, ambulance: int, token: int = Depends(current_user())):
    token = token["document_number"]
    center_query = CD.create_health_center(token, fullname, city_id, Address, specialty, email, phone_number, ambulance )
    if not center_query:
        raise HTTPException(status,code=status.HTTP_409_CONFLICT, detail="No ha sido posible realizar proceso solicitado , intente nuevamente ")
    return center_query

@app.get("/admin/receive_health_center", tags=["funtions admin"])
async def admin_receive_health_center( fullname: str, token: int = Depends(current_user())):
    token = token["document_number"]
    center_query = CD.receive_health_center(fullname)
    if not center_query:
        raise HTTPException(status,code=status.HTTP_400_BAD_REQUEST, detail="No ha sido posible realizar proceso solicitado , intente nuevamente ")
    return center_query

@app.put("/admin/update_health_center", tags=["funtions admin"])
async def admin_update_health_center(fullname: str, token: int = Depends(current_user())):
    token = token["document_number"]
    center_query = CD.update_health_center(token, fullname)
    if not center_query:
        raise HTTPException(status,code=status.HTTP_404_NOT_FOUND, detail="No ha sido posible realizar el proceso de actualizacion , intente nuevamente ")
    return center_query

@app.delete("/admin/delete_health_center", tags=["funtions admin"])
async def admin_delete_health_center(fullname: str, token: int = Depends(current_user())):
    token = token["document_number"]
    center_query = CD.delete_health_center(token, fullname)
    if not center_query:
        raise HTTPException(status,code=status.HTTP_400_BAD_REQUEST, detail="No ha sido posible eliminar el hospital indicado , por favor intentelo nuevamente ")
    return center_query


