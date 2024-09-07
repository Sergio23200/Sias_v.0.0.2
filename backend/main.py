from pydantic import BaseModel
from fastapi.security import HTTPBearer
from fastapi import HTTPException, status, Form, Depends
from datetime import date, datetime
from fastapi import FastAPI, Request, Depends, HTTPException, status, Form
from fastapi.security import OAuth2PasswordBearer,  HTTPBearer
from fastapi.responses import JSONResponse
from datetime import date, time
from aouth import create_token, validate_token
from models import Affiliate, Admin, Specialist, Hospital, Ips
import CRUD
from typing import Optional
app = FastAPI()

CD = CRUD
OAuth2_schema = OAuth2PasswordBearer(tokenUrl="login")


def get_current_Affiliate(token: str = Depends(OAuth2_schema)):
    try:
        # Validar el token y extraer los datos
        data = validate_token(token)
        if not data:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token"
            )
        user = Affiliate.get(Affiliate.email == data["email"])
        return user
    except Affiliate.DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred"
        )


def get_current_Admin(token: str = Depends(OAuth2_schema)):
    try:
        # Validar el token y extraer los datos
        data = validate_token(token)
        if not data:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token"
            )
        user = Admin.get(Admin.email == data["email"])
        return user
    except Affiliate.DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred"
        )


class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        # validad token y verificar su validez
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)

        try:
            validate = Affiliate.get(Affiliate.email == data["email"])
        except Affiliate.DoesNotExist:
            # valida si el afiliante existe en base de datos
            try:
                validate = Admin.get(Admin.email == data["email"])
            except Admin.DoesNotExist:
                raise HTTPException(
                    status_code=403, detail="Credenciales inválidas"
                    # valida si las credenciales son validas, si no aparece "credenciales inválidas"
                )

        return validate
    # validador


def model_to_dict(model_instance):
    """
    Convertir una instancia del modelo Peewee en un diccionario, manejando tipos no serializables
    """
    data = {}
    for field in model_instance._meta.sorted_field_names:
        value = getattr(model_instance, field)
        if isinstance(value, (datetime, date)):
            # Convertir fecha y hora a cadena de formato ISO
            data[field] = value.isoformat()
        else:
            data[field] = value
    return data


@ app.post("/login", tags=["auth"])
def login(email: str, password: str):
    # Intentamos autenticar al usuario como afiliado
    validate_affiliate = CD.authenticate_affiliate(email, password)
    if validate_affiliate:
        # Convertimos a dict manualmente
        affiliate_data = model_to_dict(validate_affiliate)
        token: str = create_token(affiliate_data)
        return JSONResponse(status_code=200, content={"access_token": token, "token_type": "bearer", "user_type": "affiliate"})

    # Si no es un afiliado, intentamos como administrador
    validate_admin = CD.authenticate_admin(email, password)
    if validate_admin:
        # Convertimos a dict manualmente
        admin_data = model_to_dict(validate_admin)
        token: str = create_token(admin_data)
        return JSONResponse(status_code=200, content={"access_token": token, "token_type": "bearer", "user_type": "admin"})

    # Si no es ni afiliado ni administrador, lanzamos un error
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="El usuario no está registrado"
    )


@ app.delete("/user/delete", tags=["CRUD Affiliate"], dependencies=[Depends(JWTBearer())])
async def user_delete(current_user: Affiliate = Depends(get_current_Affiliate)):
    email = current_user.email
    user_drop = CD.delete_affiliate(email)
    if not user_drop:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El proceso no se puede completar"
            # esta funcion es creada para decir que los requisitos no estan completas y aparecera "el proceso no se puede completar"
        )
    return {"detail": "El usuario ha sido eliminado"}
#esta funcion le muestra a la persona que "el usuario que ha sido eliminado"


#crear un usuario
@ app.post("/user/create", tags=["CRUD Affiliate"])
async def create_user(
    fullname: str = Form(...),
    document_type: str = Form(...),
    document_number: int = Form(...),
    birthdate: date = Form(...),
    email: str = Form(...),
    city: str = Form(...),
    password: str = Form(...),
    membership_type: str = Form(...),
    gender: str = Form(...),
    Address: str = Form(...),
    Clinical_history: str = Form(...),
    phone_number: int = Form(...)
):
    try:
        # Crear un objeto Affiliate
        user = Affiliate(
            fullname=fullname,
            document_type=document_type,
            document_number=document_number,
            birthdate=birthdate,
            email=email,
            city=city,
            password=password,
            membership_type=membership_type,
            gender=gender,
            Address=Address,
            Clinical_history=Clinical_history,
            phone_number=phone_number
        )

        # Crear el afiliado en la base de datos
        new_user = CD.create_affilite(user)

        if not new_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Error al crear el usuario")
        # esta funcion muesta si hay algun errror al crear un usuario

        return {"detail": "El usuario se ha creado con éxito"}
    # esta funcion te indica que el usuario fue creado correctamente

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error interno: {str(e)}")
    # esta funcion es cuendo el servidor presenta un error interno


@app.put("/user/update", tags=["CRUD Affiliate"], dependencies=[Depends(JWTBearer())])
async def affiliate_update(
    address: str = Form(...),
    phone_number: str = Form(...),
    city: str = Form(...),
    password: Optional[str] = Form(None),
    current_user: Affiliate = Depends(get_current_Affiliate)
):
    # Extraemos el email del usuario actual
    email = current_user.email

    # Actualizamos los datos del afiliado
    update_result = CD.update_affiliate(
        email=email,
        address=address,
        phone_number=phone_number,
        city=city,
        password=password
    )

    if not update_result:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no se pudo actualizar"
            # esta funcion te muestra cuando el usuario no se pudo actualizar
        )

    return {"detail": "Affiliate updated successfully"}
# CRUD Admin


# craer admin
@ app.post("/admin/create",  tags=["CRUD Admin"])
async def create_admin(
        fullname: str = Form(...),
        document_type: str = Form(...),
        document_number: int = Form(...),
        birthdate: date = Form(...),
        email: str = Form(...),
        first_number: str = Form(...),
        city: str = Form(...),
        password: str = Form(...),
        job_title: str = Form(...)):
    try:
        admin = Admin(fullname=fullname,
                      document_type=document_type,
                      document_number=document_number,
                      birthdate=birthdate,
                      email=email,
                      first_number=first_number,
                      city=city,
                      password=password,
                      job_title=job_title)
        new_admin = CD.create_admin(admin)
        return {"detail": "El usuario se ha creado con éxito"}
    # esta funcion te indica si el usuario es creado correctamente
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Error al crear el usuario")
    # estafuncion te indica si el usuario tuvo un error al crearse 

# eliminar admin
@app.delete("/admin/delete", tags=["CRUD Admin"], dependencies=[Depends(JWTBearer())])
async def delete_admin(current_user: Affiliate = Depends(get_current_Affiliate)):
    try:
        email = current_user.email
        rows_delete = CD.delete_Admin(email)
        return {"detail": "El usuario ha sido eliminado"}
    # esta funcion te indica que el usuario ha sido eliminado
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El proceso no se puede completar")
    # esta funcion es para cuando el proceso no se puede completar


#actualizar admin
@app.put("/admin/update", tags=["CRUD Admin"], dependencies=[Depends(HTTPBearer())])
async def update_admin(
        first_number: str = Form(...),
        city: str = Form(...),
        password: str = Form(...),
        job_title: str = Form(...),
        current_user: Admin = Depends(get_current_Admin)):
    email1 = current_user.email

    update_result = CD.update_Admin(
        email=email1,
        first_number=first_number,
        city=city,
        password=password,
        job_title=job_title
    )

    if not update_result:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no se pudo actualizar"
            # este funcion te indica de los cambios no se guardaron y aparece así "el usuario no se pudo actualizar"
        )

    return {"detail": "Affiliate updated successfully"}

# CRUD specialist


@app.post("/Specialist/create", tags=["CRUD Specialist"], dependencies=[Depends(HTTPBearer())])
async def create_Specialist(fullname: str = Form(...),
                            number_document: int = Form(...),
                            email: str = Form(...),
                            phone_number: int = Form(...),
                            specialty: str = Form(...),
                            current_user: Admin = Depends(get_current_Admin)):
    created_by = current_user.document_number  # Corregir nombre a 'created_by'

    # Crear instancia del especialista
    specialist = Specialist(
        fullname=fullname,
        number_document=number_document,
        email=email,
        phone_number=phone_number,
        specialty=specialty,
        created_by=created_by  # Cambiar 'create_by' a 'created_by'
    )

    # Usar la función correcta para crear el especialista
    new_specialist = CD.create_specialist(specialist)

    if not new_specialist:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="El especialista no pudo ser creado")
    # esta funcion te indica cuando el especialista no se pudo crear

    return {"message": "Especialista creado exitosamente"}


# actualizar specialist
@app.put("/Specialist/update", tags=["CRUD Specialist"], dependencies=[Depends(HTTPBearer())])
async def specialist_update_(number_document: int = Form(...),
                             email: str = Form(...),
                             phone_number: int = Form(...),
                             specialty: str = Form(...),):

    update_result = CD.update_specialist(
        number_document=number_document,
        email=email,
        phone_number=phone_number,
        specialty=specialty,
    )
    if not update_result:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no se pudo actualizar"
            # esta funcion te indica cuando el usuario no se pudo actualizar en su base de datos
        )

    return {"detail": "Affiliate updated successfully"}

# eliminar specialist
@app.delete("/Speialist/delete", tags=["CRUD Specialist"], dependencies=[Depends(HTTPBearer())])
async def specialist_delete(number_document: int = Form(...)):
    try:
        rows = CD.delete_specialst(number_document)
        return {"detail": "El usuario ha sido eliminado"}
    # indica que se ha eliminado correctamente el usuario
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El proceso no se puede completar")
    # esta funcion indica que el proceso no se pudo completar
    
# CRUD hospital


@app.post("/hospital/create", tags=["CRUD hospital"], dependencies=[Depends(HTTPBearer())])
async def created_Hospital(fullname: str = Form(...),
                           city: str = Form(...),
                           Address: str = Form(...),
                           email: str = Form(...),
                           phone_number: int = Form(...),
                           ambulance_dispo: int = Form(...),
                           ambulances_on_route: int = Form(...),
                           current_user: Admin = Depends(get_current_Admin)
                           ):
    created_by = current_user.document_number
    hospital = Hospital(fullname=fullname,
                        city=city,
                        Address=Address,
                        email=email,
                        phone_number=phone_number,
                        ambulance_dispo=ambulance_dispo,
                        ambulances_on_route=ambulances_on_route,
                        created_by=created_by)
    new_hospital = CD.create_Hospital(hospital)
    if not new_hospital:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="El hospital no pudo ser creado")
    # esta funcion indica que el hospital en base de datos no pudo ser creado

    return {"message": "hospital creado exitosamente"}
# esta funcion indica que el hospital fue creado exitosamente


#actualizar hospital
@app.put("/hospital/update", tags=["CRUD hospital"], dependencies=[Depends(HTTPBearer())])
async def update_Hospotal(fullname: str = Form(...),
                          email: str = Form(...),
                          phone_number: int = Form(...),
                          ambulance_dispo: int = Form(...),
                          ambulances_on_route: int = Form(...),):
    update_result = CD.update_Hospital(fullname=fullname,
                                       email=email,
                                       phone_number=phone_number,
                                       ambulance_dispo=ambulance_dispo,
                                       ambulances_on_route=ambulances_on_route,)
    if not update_result:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="El  hospital no se pudo actualizar"
            # esta funcion indica que el hospital no pudo ser actualizado
        )

    return {"detail": "el hospital updated successfully"}

# eliminar hospital
@app.delete("/hospital/update", tags=["CRUD hospital"], dependencies=[Depends(HTTPBearer())])
async def delete_Hospital(fullname: str = Form(...)):
    try:
        rows = CD.delete_hospital(fullname)
        return {"detail": "El hospital ha sido eliminado"}
    # esta funcion indica que el hospital ha sido eliminado de base de datos
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El hospital no se puede eliminar")
    # esta funcion te indica que el hospital no se ha podido eliminar
# CRUD IPS

#crear IPS
@app.post("/IPS/create", tags=["CRUD ips"], dependencies=[Depends(HTTPBearer())])
async def ips_create(fullname: str = Form(...),
                     city: str = Form(...),
                     Address: str = Form(...),
                     email: str = Form(...),
                     phone_number: int = Form(...),
                     current_user: Admin = Depends(get_current_Admin)
                     ):
    created_by = current_user.document_number
    ips = Ips(fullname=fullname,
              city=city,
              Address=Address,
              email=email,
              phone_number=phone_number,
              created_by=created_by)
    new_ips = CD.create_Hospital(ips)
    if not new_ips:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="ips no pudo ser creado")
    # esta funcion indica que el IPS no pudo ser creado

    return {"message": "ips creado exitosamente"}
# esta funcion te informa cuando el IPS es creado correctamente


#actualizar IPS
@app.put("/IPS/update", tags=["CRUD ips"], dependencies=[Depends(HTTPBearer())])
async def Ips_update(fullname: str = Form(...),
                     email: str = Form(...),
                     phone_number: int = Form(...)):
    update_result = CD.update_Ips(
        fullname=fullname,
        email=email,
        phone_number=phone_number
    )
    if not update_result:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="El  hospital no se pudo actualizar"
        )
    return {"detail": "Ips updated successfully"}
# esta funcion te informa cuando la IPS del hospita no pudo ser actualizada


# eliminar IPS
@app.delete("/IPS/update", tags=["CRUD ips"], dependencies=[Depends(HTTPBearer())])
async def delete_IPS(fullname: str = Form(...)):
    try:
        rows = CD.delete_ips(fullname)
        return {"detail": "El hospital ha sido eliminado"}
    # esta funcion informa cuando la IPS del hospital ha sido eliminada
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El hospital no se puede eliminar")
    # esta funcion te indica cuando el IPS del hospital no se puede eliminar


# CRUD medical_appointments

@app.post("/appointments/create", tags=["CRUD appointments"], dependencies=[Depends(HTTPBearer)])
async def create_appointments(appointment_type: str = Form(...),
                              fullname_affiliate: str = Form(...),
                              document_number_affiliate: int = Form(...),
                              name_doctor: str = Form(...),
                              current_user: Admin = Depends(get_current_Admin),
                              day: date = Form(...),
                              hospital_name: str = Form(...),
                              Clinical_history: str = Form(...),
                              hour: time = Form(...)):
    pass
