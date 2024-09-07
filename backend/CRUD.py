from fastapi import FastAPI
from pydantic import BaseModel
from models import Affiliate, Admin, Database, Medications
import datetime
import bcrypt
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()
oauth2 = OAuth2PasswordBearer(tokenUrl="login")


def create_admin(admin: Admin):
    try:
        hash_password = bcrypt.hashpw(
            admin.password.encode(), bcrypt.gensalt())
        admin.password = hash_password
        admin.save()
        return admin
    except:
        return None


def authenticate_affiliate(email: str, password: str):
    try:
        affiliate = Affiliate.get(Affiliate.email == email)
        if bcrypt.checkpw(password.encode(), affiliate.password.encode()):
            return affiliate
        else:
            return None

    except Affiliate.DoesNotExist:
        return None

<<<<<<< Updated upstream

def authenticete_admin(email: str, password: str):
=======
#Autentica un administrador mediante su correo electrónico y contraseña
def authenticate_admin(email: str, password: str):
>>>>>>> Stashed changes
    try:
        admin = Admin.get(Admin.email == email)
        if bcrypt.checkpw(password.encode(), admin.password.encode()):
            return admin
        else:
            return None
<<<<<<< Updated upstream
    except Admin.DoesNotExist:
        return None


def delete_affiliate(document_number: int):
    try:
        query = Affiliate.delete().where(Affiliate.document_number == document_number)
        rows_deleted = query.execute()
        if rows_deleted > 0:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False


def delete_admin(email: str):
    try:
        query = Admin.delete().where(Admin.email == email)
        rows_delete = query.execute()
        return rows_delete
    except:
        return None


def update_affiliate(document_number: int, **kwargs):
    try:
        # Buscar el afiliado en la base de datos usando el email proporcionado
        affiliate = Affiliate.get(Affiliate.document_number == document_number)

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
=======
# no se encuentra un administrador con el correo electrónico dado en la base de datos,retorna none
    except Affiliate.DoesNotExist:
>>>>>>> Stashed changes
        return None

#Autenticacion de usuario mediante su numero de documento y devuelve sus datos, esta funcion se encarga de validar el documento ingresado , si se encuentra el usuario en la base de datos devuelve su informacion por el contrario devuelve none.
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


# cracion de metodo para la creacion de usuarios# cracion de metodo para la creacion de usuarios
def create_affiliates(fullname, document_type, document_number, birthdate, email, first_number, second_number, city, password, membership_type):
    # pasar la contraseña a un hash para mayor seguridad
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    new_user = Affiliate(
        fullname=fullname,
        document_type=document_type,
        document_number=document_number,  # definicinicion de datos
        birthdate=birthdate,
        email=email,
        first_number=first_number,
        second_number=second_number,
        city=city,
        password=hashed_password.decode(),
        membership_type=membership_type
    )

    return new_user.save()

<<<<<<< Updated upstream

def create_appointment(affiliate: Affiliate, appointment_type: str, specialist: str, day: datetime.date, hospital_name: str,
                       medications: str, Clinical_history: str, hour: datetime.time):
    new_appointment = Database(
        affiliate=affiliate,
        appointment_type=appointment_type,
        specialist=specialist,
        day=day,
        hospital_name=hospital_name,
        medications=medications,
        Clinical_history=Clinical_history,
        hour=hour
    )
    return new_appointment.save()


def delete_medications(generic_name: str):
    query_medications = Medications.delete().where(
        Medications.generic_name == generic_name)
    if not query_medications:
=======
    arg:
        token: int
    return:
        true si el usuario se elimino
        Flase si el usurio no se elimino
    except:
        print(f"Error: {e}")
>>>>>>> Stashed changes
        return False
    return True
# funtions admin


def delete_m(document_number: int, generic_name: str):
    pass


def update_m(document_number: str, **keys):
    pass


def create_m(document_number: str, medico: Medications):
    pass


def read_m(generic_name: str):
    pass

#funtions adm hospital
def create_hospital(document_number: int, fullname: str, city_id: str,  Address: str, specialty: str, email: str, phone_number: int, ambulance: int ):
    pass

<<<<<<< Updated upstream
def receive_hospital(document_number: int, fullname: str):
    pass

def update_hospital(document_number: int, fullname: str, **keys):
    pass
=======
#crea un nuevo administrador con la contraseña y lo guarda en la base de datos.
#si en el proceso ocurre un error al guardar el nuevo admin este se encarga de capturar las excepciones e imprimirlas . 
def create_admin(admin: Admin):
    try:
        hash_password = bcrypt.hashpw(
            admin.password.encode(), bcrypt.gensalt())
        admin.password = hash_password
        admin.save()
        return admin
    
    #Este se imprime si ocurre en la base de datos como una violacion a claves de id unico . 
    except IntegrityError as e:
        print(f"error IntegrityError {e}")
    #Se imprimira si ocurre algun otro error general en la base de datos
    except DatabaseError as e:
        print(f"error en la base de datos {e}")
>>>>>>> Stashed changes

def delete_hospital(document_number: int, fullname: str):
    pass

<<<<<<< Updated upstream
#funtions adm centros medicos 
=======
#Esta funcion se encarga de eliminar un administrador por medio de su correo electronico . si este proceso es exitoso devolvera true , sino encuentra ningun administrados con el correo indicado este devolvera false e indicara un mensaje de error . 
>>>>>>> Stashed changes

def create_health_center(document_number: int, fullname: str, city_id: str,  Address: str, specialty: str, email: str, phone_number: int, ambulance: int ):
    pass

def receive_health_center(document_number: int, fullname: str):
    pass

def update_health_center(document_number: int, fullname: str, **keys):
    pass

<<<<<<< Updated upstream
def delete_health_center(document_number: int, fullname: str):
    pass
=======
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

#crea una cita medica en la base de datos luego de validar los datos.Esta funcion verifica el afiliado , la clinica y el especialista , que existan en la vase de datos . si todos los datos proporcionados son correctos este guardara la nueva cita en la base de datos de lo contrario no guardara y nos retorna none. 
def create_appointments(appointments: medical_appointments):
    try:
        new_appointments = appointments
        authenticate_affiliates = Affiliate.get((Affiliate.fullname == appointments.fullname_affiliate) &
                                                (Affiliate.document_number == appointments.document_number_affiliate) &
                                                (Affiliate.Clinical_history == appointments.Clinical_history))
        # si la validacion en alguno de los datos ingresados es incorrecta retornará none.
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
        #si todos los datos ingresados son correctos se creara la nueva cita generada y la guardara en la base de datos . 
        return new_appointments.save()
    #se imprimira esta excepcion si no se encuentra el afiliado ingresado . 
    except DoesNotExist:
        print("El afiliado no existe en la base de datos.")
        return None
    #Se imprimirá esta excepcion si se encuentra algun error al guardar la informacion como datos duplicados .
    except IntegrityError as e:
        print(f"error IntegrityError {e}")
    #Se imprimirá si registra algun error general en nuestra base de datos.
    except DatabaseError as e:
        print(f"error en la base de datos {e}")
    #imprime cualquier otro error .
    except Exception as e:
        print(f"Error desconocio : {e}")

#Actualiza datos de una cita ya existente en nuestra base de datos . 
#La cita sera buscada por su ID **el cual sera el identificador unico de la cita que se desea actualizar** y si los datos son correctos actualizará los datos proporcionados en kwargs*campos que se desea actualizar en la cita.
def update_appointments(id: int, **kwargs):
    try:
        appointment = medical_appointments.get(medical_appointments.id == id)
#si los datos son validos y la cita es encontrada , se guardaran los cambios realizados . 
        for key, value in kwargs.items():
            if hasattr(appointment, key):
                setattr(appointment, key, value)

        appointment.save()
        return appointment
#Si el *ID* es incorrecto o si ocurre algun error , no se actualizará ningun cambio y nos retornará un none . 
    except DoesNotExist:
        return None
    except Exception as e:
        print(f"Error al actualizar la cita: {e}")
        return None


#Esta funcion se encarga de eliminar una cita luego de que el usuario realice el paso de autenticacion .
def delete_appointments(id: int, token: int):
#validacion de usuario mediante el token , nos retornara :
# true si la cita se eliminó con exito 
#  false si la cita no pudo ser eliminada  
#  none si la autenticacion de usuario falla . 
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
#Imprimirá esta excepcion si la cita o el afiliado no existen en la base de datos 
    except DoesNotExist:
        print("El afiliado no existe en la base de datos.")
        return None
#Imprimirá esta excepcion si hay algun error de integridad en la base de datos.
    except IntegrityError as e:
        print(f"error IntegrityError {e}")
#Imprimirá esta excepcion con algun error en general con la base de datos.
    except DatabaseError as e:
        print(f"error en la base de datos {e}")
#Esta excepcion imprimira algun error no previsto . 
    except Exception as e:
        print(f"Error desconocio : {e}")


# CRUD specialist

# Esta funcion se encargará de crear un nuevo especialista en la base de datos.

def create_specialist(specialist: Specialist):
    try:
        # Guardar el especialista
        new_specialist = specialist.save() 
        # Retornar el objeto especialista creado y ya guardado en la base de datos
        return new_specialist 
#De no ser exitosa la creacion del nuevo especialista en la base de datos nos retornara las siguientes excepciones con errores HTTP
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


#Esta funcion actualizará los datos de un especialista ya existente en la base de datos . 
#El especialista sera buscado por su numero de documento y los campos a acualizar seran en los kwargs
def update_specialist(number_document: int, **kwargs):
    try:#si el especialista es encontrado y los datos ingresados son validos, se guardaran los cambios.
        specialist = Specialist.get(
            Specialist.number_document == number_document)

        for key, value in kwargs.items():
            if hasattr(specialist, key):
                setattr(specialist, key, value)

        specialist.save()
        return specialist#retornara el objeto especialista actualizado y guardado en la base de datos . 
    except DoesNotExist:#si no encuentra especialista con el numero de documento ingresado . retornara none. 
        return None
    #captura cualquier otro error que pueda ocurrir al actualizar datos , el cual imprimira un error y retorna none . 
    except Exception as e:
        print(f"Error al actualizar la cita: {e}")
        return None

#Esta funcion se encargará de eliminar algun especialista de la base de datos utilizando en numero de documento 
def delete_specialst(number_document: int):
    try: #eliminacion exitosa . 
        query = Specialist.delete().where(Specialist.number_document == number_document)
        rows_deleted = query.execute()
        if rows_deleted > 0:
            return True
        else:
            return False #no se encuentra ningun especialista con el documento ingresado o no fue posible eliminar .
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

# Esta funcion se encargará de crear un nuevo hospital en la base de datos.

def create_Hospital(hospital: Hospital):
    try: # Guardará nuevo hospital.
        new_hospital = hospital
        # Retornar el objeto Hospital creado y ya guardado en la base de datos
        return new_hospital.save()
#De no ser exitosa la creacion del nuevo Hospital en la base de datos nos retornara las siguientes excepciones con errores HTTP
    except DoesNotExist:
        print("El afiliado no existe en la base de datos.")
        return None
    except IntegrityError as e:
        print(f"error IntegrityError {e}")
    except DatabaseError as e:
        print(f"error en la base de datos {e}")
    except Exception as e:
        print(f"Error desconocio : {e}")

#Esta funcion actualizará los datos de algun Hospital ya existente en la base de datos . 
#El Hospital  será buscado por su nombre y los campos a acualizar seran en los kwargs
def update_Hospital(fullname: str, **kwargs):
    try:#si el Hospital es encontrado y los datos ingresados son validos, se guardaran los cambios.
        hospital = Hospital.get(Hospital.fullname == fullname)

        for key, value in kwargs.items():
            if hasattr(hospital, key):
                setattr(hospital, key, value)

        hospital.save()
        return hospital#retornará el objeto Hospital actualizado y guardado en la base de datos 
    except DoesNotExist:#si no encuentra algun Hospital por el nombre ingresado. retornara none. 
        return None
    except Exception as e:#captura cualquier otro error que pueda ocurrir al actualizar datos -Hospital , el cual imprimira un error y retorna none .
        print(f"Error al actualizar la cita: {e}")
        return None

#Esta funcion se encargará de eliminar algun Hospital de la base de datos utilizando su nombre .
def delete_hospital(fullname: int):
    try:#eliminacion exitosa . 
        query = Hospital.delete().where(Hospital.fullname == fullname)
        rows_deleted = query.execute()
        if rows_deleted > 0:
            return True
        else:
            return False #no se encuentra ningun Hospital con el nombre ingresado o no fue posible eliminar .
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

# Esta funcion se encargará de crear una Ips en la base de datos.
def create_Ips(ips: Ips):
    try:# Guardará nueva ips ingresada.
        new_ips = ips
        return new_ips.save()

#De no ser exitosa la creacion de una nueva ips en la base de datos nos retornara las siguientes excepciones con errores HTTP
    except DoesNotExist:
        print("El afiliado no existe en la base de datos.")
        return None
    except IntegrityError as e:
        print(f"error IntegrityError {e}")
    except DatabaseError as e:
        print(f"error en la base de datos {e}")
    except Exception as e:
        print(f"Error desconocio : {e}")

#Esta funcion se encargará de eliminar alguna eps ya existente en la base de datos utilizando su id  .

def delete_ips(id: int):
    try: #eliminacion exitosa . 
        query = Ips.delete().where(Ips.id == id)
        rows_deleted = query.execute()
        if rows_deleted > 0:
            return True
        else:
            return False #no se encuentra ninguna ips con el id ingresado o no fue posible eliminarlo .
    except DoesNotExist:
        print("El afiliado no existe en la base de datos.")
        return None
    except IntegrityError as e:
        print(f"error IntegrityError {e}")
    except DatabaseError as e:
        print(f"error en la base de datos {e}")
    except Exception as e:
        print(f"Error desconocio : {e}")

#Esta funcion actualizará los datos de alguna ips ya existente en la base de datos . esta será buscada por su nombre y los campos a acualizar seran en los kwargs
def update_Ips(fullname: str, **kwargs):
    try:#si la ips es encontrada y los datos ingresados son validos, se guardaran los cambios.
        ips = Ips.get(Ips.fullname == fullname)

        for key, value in kwargs.items():
            if hasattr(ips, key):
                setattr(ips, key, value)

        ips.save()#guardará los cambios en los items relacionados.
        return ips #retornará el objeto ips actualizado y guardado en la base de datos 
    except DoesNotExist:
        return None
    except Exception as e:
        print(f"Error al actualizar la cita: {e}")
        return None

# CRUD Medications

#Esta funcion nos permitira crear una nueva entrada de medicamento en la base de datos, tendremos como parametros el token y el objeto a medicamento el cual se guardará .
# en esta funcion el usuario se debe autenticar con el token .
#si hay una autenticacion correcta se guardara el objeto medicamentos en la base de datos .
#De no tener una autenticacion exitosa , imprimira el error correspondiente . 
def create_medications(token: int, medications: Medications):
    try:
        authenticate = token_oaut(token)
        if not authenticate:
            return print("la persona no esta autenticada")
        new_medications = medications
        return new_medications.save()#Registro de nuevo medicamento exitoso
    except DoesNotExist:
        print("El afiliado no existe en la base de datos.")
        return None #existe algun error en la creacion del nuevo medicamento o con una autenticacion fallida . 
    except IntegrityError as e:
        print(f"error IntegrityError {e}")
    except DatabaseError as e:
        print(f"error en la base de datos {e}")
    except Exception as e:
        print(f"Error desconocio : {e}")

#Esta funcion se encargará de actualizar un medicamento ya existente en la base de datos . 
# Esta funcion autenticará primero al usuario con el token.
# se realizara la busqueda del medicamento el cual se actualizará por medio de su ID. 
# Se actualizaran los datos con los valores indicador en los kwargs 
def update_medications(token: int, id: int, **kwargs):
    try:
        authenticate = token_oaut(token)
        if not authenticate:
            return print("la persona no esta autenticada")
        medications = Medications.get(Medications.id == id)

        for key, value in kwargs.items():
            if hasattr(medications, key):
                setattr(medications, key, value)

        medications.save()#Actualizacion exitosa . 
        return medications
    except DoesNotExist:
        return None #medicamento con ID proporcionado no existe en la base de datos . 
    except Exception as e:
        print(f"Error al actualizar la cita: {e}")#se obtiene algun error inesperado . 
        return None

#Esta funcion eliminara algun medicamento en la base de datos . el cual se obtendra acceso a el por medio de su ID . 
# Esta funcion autenticará primero al usuario con el token.
# se realizara la busqueda del medicamento el cual se actualizará por medio de su ID. 
def delete_medications(id: int, token: int):
    try:
        authenticate = token_oaut(token)
        if not authenticate:
            return print("la persona no esta autenticada")
        query = Medications.delete().where(Medications.id == id)#eliminacion del mismo será exitosa. 
        rows_deleted = query.execute()
        if rows_deleted > 0:
            return True#medicamento eliminado correctamente.
        else:
            return False#No fue posible encontrar algun medicamento con el ID ingresado para eliminar . 
    except DoesNotExist:
        print("El afiliado no existe en la base de datos.")
        return None # algun error que pueda aparecer durante la eliminacion. 
    except IntegrityError as e:
        print(f"error IntegrityError {e}")
    except DatabaseError as e:
        print(f"error en la base de datos {e}")
    except Exception as e:
        print(f"Error desconocio : {e}")

# Esta funcion se encarga de disminuir la cantidad disponible de algun medicamento en la base de datos . esta funcion realizará : 
# Autenticacion del usuario con el token. 
# Buscara el medicamento por el nombre generico ingresado . 
# Indicará la cantidad disponible de ese medicamento ingresado , especificada en la parte stock , si la cantidad llega a 0<= aparecera NO DISPONIBLE . 
def decrease_stock(token: int, generic_name: str, stock: int):
    try:#Autenticacion 
        authenticate = token_oaut(token)
        if not authenticate:
            print("La persona no está autenticada")
            return None # si la autenticacion no esta autenticada correctamente no podra acceder a los datos . 

        search = Medications.get(Medications.generic_name == generic_name)

        if not search:
            print("El nombre del medicamento no está en la base de datos")
            return None

        if not search.available:  # Corregido 'aviable' a 'available'
            print("El medicamento se encuentra agotado")
            return None

        search.stocks -= stock
# Indicará la cantidad disponible de ese medicamento ingresado , especificada en la parte stock , si la cantidad llega a 0<= aparecera NO DISPONIBLE . 
        if search.stocks <= 0:
            search.stocks = 0
            search.available = False

        search.save()
        return search

    except Medications.DoesNotExist:
        print("El medicamento no existe en la base de datos.")
        return None# error durante el proceso o producto no disponible . 
    except IntegrityError as e:
        print(f"Error de integridad: {e}")
    except DatabaseError as e:
        print(f"Error en la base de datos: {e}")
    except Exception as e:
        print(f"Error desconocido: {e}")
>>>>>>> Stashed changes
