from fastapi import FastAPI
from pydantic import BaseModel
from models import Affiliate, Admin
import datetime
import bcrypt
from fastapi.security import OAuth2PasswordBearer
app = FastAPI()
oauth2 = OAuth2PasswordBearer(tokenUrl = "login")
class User(BaseModel):
    username: str
    fullname: str
    email: str
    disable: bool

def create_admin(admin:Admin):
    try:
        hash_password = bcrypt.hashpw(admin.password.encode(), bcrypt.gensalt())
        admin.password = hash_password
        admin.save()
        return admin
    except:
         return None

def authenticate_affiliate(email: str , password: str):
    try:
         affiliate = Affiliate.get(Affiliate.email == email)
         if bcrypt.checkpw(password.encode(), affiliate.password.encode()):
            return affiliate
         else:
              return None
         
    except Affiliate.DoesNotExist:
        return None 
def authenticete_admin(email: str, password: str):
     try:
          admin = Admin.get(Admin.email == email)
          if bcrypt.checkpw(password.encode(), admin.password.encode()):
               return admin
          else:
               return None
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
def delete_admin(email:str):
     try:
          query = Admin.delete().where(Admin.email == email)
          rows_delete = query.execute()
          return rows_delete
     except:
          return None
def update_affiliate(email:str, **kwargs):
    try:
        # Buscar el afiliado en la base de datos usando el email proporcionado
        affiliate = Affiliate.get(Affiliate.email == email)

        # Iterar sobre los argumentos proporcionados en kwargs
        for key, value in kwargs.items():
            # Verificar si el modelo tiene un atributo con el nombre de la clave
            if hasattr(affiliate, key):
                # Si la clave es 'password', hacer hash de la nueva contraseña
                if key == 'password':
                    affiliate.password = bcrypt.hashpw(value.encode(), bcrypt.gensalt()).decode()
                else:
                    # Para otros campos, simplemente asignar el nuevo valor
                    setattr(affiliate, key, value)
        
        # Guardar los cambios en la base de datos
        affiliate.save()
    except:
         return None
def update_Admin(email:str, **kwargs):
    try:
        # Buscar el afiliado en la base de datos usando el email proporcionado
        Admin = Admin.get(Admin.email == email)

        # Iterar sobre los argumentos proporcionados en kwargs
        for key, value in kwargs.items():
            # Verificar si el modelo tiene un atributo con el nombre de la clave
            if hasattr(Admin, key):
                # Si la clave es 'password', hacer hash de la nueva contraseña
                if key == 'password':
                    Admin.password = bcrypt.hashpw(value.encode(), bcrypt.gensalt()).decode()
                else:
                    # Para otros campos, simplemente asignar el nuevo valor
                    setattr(Admin, key, value)
        
        # Guardar los cambios en la base de datos
        Admin.save()
    except:
         return None
def token_oaut(number_document: str):
    try:
        authenticate = Affiliate.get(Affiliate.document_number== number_document)
        if not authenticate:
            return None
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
def create_affiliates(fullname, document_type, document_number, birthdate, email, first_number, second_number, city, password, membership_type):# cracion de metodo para la creacion de usuarios# cracion de metodo para la creacion de usuarios
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())  # pasar la contraseña a un hash para mayor seguridad
    new_user = Affiliate(
        fullname=fullname,
        document_type=document_type,
        document_number=document_number, # definicinicion de datos 
        birthdate=birthdate,
        email=email,
        first_number=first_number,
        second_number=second_number,
        city=city,
        password=hashed_password.decode(),
        membership_type=membership_type
    )
    
    return new_user.save()

