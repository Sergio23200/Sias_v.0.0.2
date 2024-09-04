from peewee import DoesNotExist
from fastapi import FastAPI
from pydantic import BaseModel
from models import Affiliate, Admin, medical_appointments, Medications, Specialist, Hospital, Ips
from peewee import IntegrityError, DatabaseError
import datetime
import bcrypt
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()
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


def delete_affiliate(token: int):
    try:
        query = Affiliate.delete().where(Affiliate.document_number == token)
        rows_deleted = query.execute()
        if rows_deleted > 0:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False


def update_affiliate(token: int, **kwargs):
    try:
        # Buscar el afiliado en la base de datos usando el email proporcionado
        affiliate = Affiliate.get(Affiliate.document_number == token)

        # Iterar sobre los argumentos proporcionados en kwargs
        for key, value in kwargs.items():
            # Verificar si el modelo tiene un atributo con el nombre de la clave
            if hasattr(affiliate, key):
                # Si la clave es 'password', hacer hash de la nueva contraseña
                if key == 'password':
                    affiliate.password = bcrypt.hashpw(
                        value.encode(), bcrypt.gensalt()).decode()
                else:
                    # Para otros campos, simplemente asignar el nuevo valor
                    setattr(affiliate, key, value)

        # Guardar los cambios en la base de datos
        affiliate.save()
    except:
        return None


def create_affilite(affilite: Affiliate):
    try:
        hash_password = bcrypt.hashpw(
            affilite.password.encode(), bcrypt.gensalt())
        affilite.password = hash_password
        affilite.save()
        return affilite
    except IntegrityError as e:
        print(f"error IntegrityError {e}")
    except DatabaseError as e:
        print(f"error en la base de datos {e}")

    except Exception as e:
        print(f"Error desconocio : {e}")

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


def delete_Admin(token: int):
    try:
        query = Admin.delete().where(Admin.document_number == token)
        rows_deleted = query.execute()
        if rows_deleted > 0:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False


def update_Admin(email: str, **kwargs):
    try:
        # Buscar el afiliado en la base de datos usando el email proporcionado
        Admin = Admin.get(Admin.email == email)

        # Iterar sobre los argumentos proporcionados en kwargs
        for key, value in kwargs.items():
            # Verificar si el modelo tiene un atributo con el nombre de la clave
            if hasattr(Admin, key):
                # Si la clave es 'password', hacer hash de la nueva contraseña
                if key == 'password':
                    Admin.password = bcrypt.hashpw(
                        value.encode(), bcrypt.gensalt()).decode()
                else:
                    # Para otros campos, simplemente asignar el nuevo valor
                    setattr(Admin, key, value)

        # Guardar los cambios en la base de datos
        return Admin.save()
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


def create_specialist(token: int, specialist: Specialist):
    try:
        authenticate = token_oaut(token)
        if not authenticate:
            return print("la persona no esta autenticada")
        new_specialist = specialist
        return new_specialist.save()
    except DoesNotExist:
        print("El afiliado no existe en la base de datos.")
        return None
    except IntegrityError as e:
        print(f"error IntegrityError {e}")
    except DatabaseError as e:
        print(f"error en la base de datos {e}")
    except Exception as e:
        print(f"Error desconocio : {e}")


def update_specialist(token: int, id: int, **kwargs):
    try:
        authenticate = token_oaut(token)
        if not authenticate:
            return print("la persona no esta autenticada")
        specialist = Specialist.get(Specialist.id == id)

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

# CRUD Hospital


def create_Hospital(token: int, hospital: Hospital):
    try:
        authenticate = token_oaut(token)
        if not authenticate:
            return print("la persona no esta autenticada")
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


def update_Hospital(token: int, id: int, **kwargs):
    try:
        authenticate = token_oaut(token)
        if not authenticate:
            return print("la persona no esta autenticada")
        hospital = Hospital.get(Hospital.id == id)

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


def delete_hospital(id: int, token: int):
    try:
        authenticate = token_oaut(token)
        if not authenticate:
            return print("la persona no esta autenticada")
        query = Hospital.delete().where(Hospital.id == id)
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


def create_Ips(token: int, ips: Ips):
    try:
        authenticate = token_oaut(token)
        if not authenticate:
            return print("la persona no esta autenticada")
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


def update_Hospital(token: int, id: int, **kwargs):
    try:
        authenticate = token_oaut(token)
        if not authenticate:
            return print("la persona no esta autenticada")
        ips = Ips.get(Ips.id == id)

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


def delete_ips(id: int, token: int):
    try:
        authenticate = token_oaut(token)
        if not authenticate:
            return print("la persona no esta autenticada")
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
