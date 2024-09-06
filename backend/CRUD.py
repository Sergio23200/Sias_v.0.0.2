from peewee import DoesNotExist
from fastapi import HTTPException, status
from pydantic import BaseModel
from models import Affiliate, Admin, medical_appointments, Medications, Specialist, Hospital, Ips
from peewee import IntegrityError, DatabaseError
import datetime
import bcrypt
from fastapi.security import OAuth2PasswordBearer

oauth2 = OAuth2PasswordBearer(tokenUrl="login")


# autenticacion y validacion

def authenticate_affiliate(email: str, password: str):
    try:
        affiliate = Affiliate.get(Affiliate.email == email)
        if bcrypt.checkpw(password.encode(), affiliate.password.encode()):
            return affiliate
        else:
            return None

    except Affiliate.DoesNotExist:
        return None


def authenticate_admin(email: str, password: str):
    try:
        admin = Admin.get(Admin.email == email)
        if bcrypt.checkpw(password.encode(), admin.password.encode()):
            return admin
        else:
            return None

    except Affiliate.DoesNotExist:
        return None


def token_oaut(document_number: str):
    try:
        authenticate = Affiliate.get(
            Affiliate.document_number == document_number)
        if not authenticate:
            authenticate = Admin.get(
                Admin.document_number == document_number)
            if not authenticate:
                return None
            admin_data = {
                "fullname": authenticate.fullname,
                "document_type": authenticate.document_type,
                "document_number": authenticate.document_number,
                "birthdate": authenticate.birthdate,
                "email": authenticate.email,
                "first_number": authenticate.first_number,
                "second_number": authenticate.second_number,
                "city": authenticate.city,
                "job_title": authenticate.job_title
            }
            return admin_data
        affiliate_data = {
            "id": authenticate.id,
            "fullname": authenticate.fullname,
            "document_type": authenticate.document_type,
            "document_number": authenticate.document_number,
            "birthdate": authenticate.birthdate,
            "gender": authenticate.gender,
            "email": authenticate.email,
            "Address": authenticate.Address,
            "phone_number": authenticate.phone_number,
            "city": authenticate.city,
            "membership_type": authenticate.membership_type,
            "created_date": authenticate.created_date
        }
        return affiliate_data
    except:
        print("error directo al servidor ")
# CRUD  affiliate:


def delete_affiliate(email: str):
    """ 
    esta funcion fue creada para eliminar registros de la tabla afiliados:

    por medio del token se hace la busqueda del usuario a eliminar y se retorna,
    si el usuario no existe se retornara flase.

    arg:
        token: int
    return:
        true si el usuario se elimino
        Flase si el usurio no se elimino
    except:
           print(f"Error: {e}")
        return False

    """
    try:
        query = Affiliate.delete().where(Affiliate.email == email)
        rows_deleted = query.execute()
        if rows_deleted > 0:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False


def update_affiliate(**kwargs):
    try:
        # Buscar el afiliado en la base de datos usando el email proporcionado
        affiliate = Affiliate.get(Affiliate.email == kwargs.get('email'))

        # Iterar sobre los argumentos proporcionados en kwargs
        for key, value in kwargs.items():
            if hasattr(affiliate, key):
                if key == 'password':
                    affiliate.password = bcrypt.hashpw(
                        value.encode(), bcrypt.gensalt()).decode()
                else:
                    setattr(affiliate, key, value)

        # Guardar los cambios en la base de datos
        affiliate.save()
        return affiliate
    except:
        return None


def create_affilite(affiliate: Affiliate):
    try:
        # Hashear la contraseña
        hash_password = bcrypt.hashpw(
            affiliate.password.encode(), bcrypt.gensalt())
        affiliate.password = hash_password

        # Guardar el afiliado en la base de datos
        affiliate.save()
        return affiliate
    except IntegrityError as e:
        print(f"Error de Integridad: {e}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Error de integridad de datos.")
    except DatabaseError as e:
        print(f"Error en la base de datos: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error en la base de datos.")
    except Exception as e:
        print(f"Error desconocido: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error desconocido.")

# CRUD Admin


def create_admin(admin: Admin):
    try:
        hash_password = bcrypt.hashpw(
            admin.password.encode(), bcrypt.gensalt())
        admin.password = hash_password
        admin.save()
        return admin
    except IntegrityError as e:
        print(f"error IntegrityError {e}")
    except DatabaseError as e:
        print(f"error en la base de datos {e}")

    except Exception as e:
        print(f"Error desconocio : {e}")


def delete_Admin(email: str):
    try:
        query = Admin.delete().where(Admin.email == email)
        rows_deleted = query.execute()
        if rows_deleted > 0:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False


def update_Admin(**kwargs):
    try:
        # Buscar el afiliado en la base de datos usando el email proporcionado
        admin = Admin.get(Admin.email == kwargs.get('email'))

        # Iterar sobre los argumentos proporcionados en kwargs
        for key, value in kwargs.items():
            if hasattr(admin, key):
                if key == 'password':
                    admin.password = bcrypt.hashpw(
                        value.encode(), bcrypt.gensalt()).decode()
                else:
                    setattr(admin, key, value)

        # Guardar los cambios en la base de datos
        admin.save()
        return admin
    except:
        return None
# CRUD appointments


def create_appointments(appointments: medical_appointments):
    try:
        new_appointments = appointments
        authenticate_affiliates = Affiliate.get((Affiliate.fullname == appointments.fullname_affiliate) &
                                                (Affiliate.document_number == appointments.document_number_affiliate) &
                                                (Affiliate.Clinical_history == appointments.Clinical_history))
        if not authenticate_affiliates:
            return None
        authenticate_especialist = Specialist.get(
            (Specialist.fullname == appointments.name_doctor) & (Specialist.specialty == appointments.appointment_type))
        if not authenticate_especialist:
            return None
        authenticate_hospital = Hospital.get(
            Hospital.fullname == appointments.hospital_name)
        if not authenticate_hospital:
            return None
        return new_appointments.save()
    except DoesNotExist:
        print("El afiliado no existe en la base de datos.")
        return None
    except IntegrityError as e:
        print(f"error IntegrityError {e}")
    except DatabaseError as e:
        print(f"error en la base de datos {e}")
    except Exception as e:
        print(f"Error desconocio : {e}")


def update_appointments(id: int, **kwargs):
    try:
        appointment = medical_appointments.get(medical_appointments.id == id)

        for key, value in kwargs.items():
            if hasattr(appointment, key):
                setattr(appointment, key, value)

        appointment.save()
        return appointment
    except DoesNotExist:
        return None
    except Exception as e:
        print(f"Error al actualizar la cita: {e}")
        return None


def delete_appointments(id: int, token: int):
    try:
        authenticate = token_oaut(token)
        if not authenticate:
            return print("la persona no esta autenticada")
        query = medical_appointments.delete().where(medical_appointments.id == id)
        rows_deleted = query.execute()
        if rows_deleted > 0:
            return True
        else:
            return False
    except DoesNotExist:
        print("El afiliado no existe en la base de datos.")
        return None
    except IntegrityError as e:
        print(f"error IntegrityError {e}")
    except DatabaseError as e:
        print(f"error en la base de datos {e}")
    except Exception as e:
        print(f"Error desconocio : {e}")


# CRUD specialist


def create_specialist(specialist: Specialist):
    try:
        new_specialist = specialist.save()  # Guardar el especialista
        return new_specialist  # Retornar el objeto creado
    except DoesNotExist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="El afiliado no existe en la base de datos")
    except IntegrityError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Error de integridad: {e}")
    except DatabaseError as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Error en la base de datos: {e}")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Error desconocido: {e}")


def update_specialist(number_document: int, **kwargs):
    try:
        specialist = Specialist.get(
            Specialist.number_document == number_document)

        for key, value in kwargs.items():
            if hasattr(specialist, key):
                setattr(specialist, key, value)

        specialist.save()
        return specialist
    except DoesNotExist:
        return None
    except Exception as e:
        print(f"Error al actualizar la cita: {e}")
        return None


def delete_specialst(number_document: int):
    try:
        query = Specialist.delete().where(Specialist.number_document == number_document)
        rows_deleted = query.execute()
        if rows_deleted > 0:
            return True
        else:
            return False
    except DoesNotExist:
        print("El afiliado no existe en la base de datos.")
        return None
    except IntegrityError as e:
        print(f"error IntegrityError {e}")
    except DatabaseError as e:
        print(f"error en la base de datos {e}")
    except Exception as e:
        print(f"Error desconocio : {e}")

# CRUD Hospital


def create_Hospital(hospital: Hospital):
    try:
        new_hospital = hospital
        return new_hospital.save()
    except DoesNotExist:
        print("El afiliado no existe en la base de datos.")
        return None
    except IntegrityError as e:
        print(f"error IntegrityError {e}")
    except DatabaseError as e:
        print(f"error en la base de datos {e}")
    except Exception as e:
        print(f"Error desconocio : {e}")


def update_Hospital(fullname: str, **kwargs):
    try:
        hospital = Hospital.get(Hospital.fullname == fullname)

        for key, value in kwargs.items():
            if hasattr(hospital, key):
                setattr(hospital, key, value)

        hospital.save()
        return hospital
    except DoesNotExist:
        return None
    except Exception as e:
        print(f"Error al actualizar la cita: {e}")
        return None


def delete_hospital(fullname: int):
    try:
        query = Hospital.delete().where(Hospital.fullname == fullname)
        rows_deleted = query.execute()
        if rows_deleted > 0:
            return True
        else:
            return False
    except DoesNotExist:
        print("El afiliado no existe en la base de datos.")
        return None
    except IntegrityError as e:
        print(f"error IntegrityError {e}")
    except DatabaseError as e:
        print(f"error en la base de datos {e}")
    except Exception as e:
        print(f"Error desconocio : {e}")

# CRUD IPS


def create_Ips(ips: Ips):
    try:
        new_ips = ips
        return new_ips.save()
    except DoesNotExist:
        print("El afiliado no existe en la base de datos.")
        return None
    except IntegrityError as e:
        print(f"error IntegrityError {e}")
    except DatabaseError as e:
        print(f"error en la base de datos {e}")
    except Exception as e:
        print(f"Error desconocio : {e}")


def delete_ips(id: int):
    try:
        query = Ips.delete().where(Ips.id == id)
        rows_deleted = query.execute()
        if rows_deleted > 0:
            return True
        else:
            return False
    except DoesNotExist:
        print("El afiliado no existe en la base de datos.")
        return None
    except IntegrityError as e:
        print(f"error IntegrityError {e}")
    except DatabaseError as e:
        print(f"error en la base de datos {e}")
    except Exception as e:
        print(f"Error desconocio : {e}")


def update_Ips(fullname: str, **kwargs):
    try:
        ips = Ips.get(Ips.fullname == fullname)

        for key, value in kwargs.items():
            if hasattr(ips, key):
                setattr(ips, key, value)

        ips.save()
        return ips
    except DoesNotExist:
        return None
    except Exception as e:
        print(f"Error al actualizar la cita: {e}")
        return None

# CRUD Medications


def create_medications(token: int, medications: Medications):
    try:
        authenticate = token_oaut(token)
        if not authenticate:
            return print("la persona no esta autenticada")
        new_medications = medications
        return new_medications.save()
    except DoesNotExist:
        print("El afiliado no existe en la base de datos.")
        return None
    except IntegrityError as e:
        print(f"error IntegrityError {e}")
    except DatabaseError as e:
        print(f"error en la base de datos {e}")
    except Exception as e:
        print(f"Error desconocio : {e}")


def update_medications(token: int, id: int, **kwargs):
    try:
        authenticate = token_oaut(token)
        if not authenticate:
            return print("la persona no esta autenticada")
        medications = Medications.get(Medications.id == id)

        for key, value in kwargs.items():
            if hasattr(medications, key):
                setattr(medications, key, value)

        medications.save()
        return medications
    except DoesNotExist:
        return None
    except Exception as e:
        print(f"Error al actualizar la cita: {e}")
        return None


def delete_ips(id: int, token: int):
    try:
        authenticate = token_oaut(token)
        if not authenticate:
            return print("la persona no esta autenticada")
        query = Medications.delete().where(Medications.id == id)
        rows_deleted = query.execute()
        if rows_deleted > 0:
            return True
        else:
            return False
    except DoesNotExist:
        print("El afiliado no existe en la base de datos.")
        return None
    except IntegrityError as e:
        print(f"error IntegrityError {e}")
    except DatabaseError as e:
        print(f"error en la base de datos {e}")
    except Exception as e:
        print(f"Error desconocio : {e}")


def decrease_stock(token: int, generic_name: str, stock: int):
    try:
        authenticate = token_oaut(token)
        if not authenticate:
            print("La persona no está autenticada")
            return None

        search = Medications.get(Medications.generic_name == generic_name)

        if not search:
            print("El nombre del medicamento no está en la base de datos")
            return None

        if not search.available:  # Corregido 'aviable' a 'available'
            print("El medicamento se encuentra agotado")
            return None

        search.stocks -= stock

        if search.stocks <= 0:
            search.stocks = 0
            search.available = False

        search.save()
        return search

    except Medications.DoesNotExist:
        print("El medicamento no existe en la base de datos.")
        return None
    except IntegrityError as e:
        print(f"Error de integridad: {e}")
    except DatabaseError as e:
        print(f"Error en la base de datos: {e}")
    except Exception as e:
        print(f"Error desconocido: {e}")
