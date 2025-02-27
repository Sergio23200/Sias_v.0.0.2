from schemas.admin_schema import Admin_schema, Admin_update, admin_filter_schema
from fastapi.responses import JSONResponse
import bcrypt
from models.Admin import Admin_model
from schemas.login_schema import login_schema_sign_up


class Admin_service():
    def __init__(self, db) -> None:
        self.db = db

    def get_admin(self):
        """
        esta funcion crea un registro de tipo admin utilizando el archivo en el paquete de schema,
        con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
        seguridad ya que los admins tienen varios permisos, luego de valiadar, si el token no es correcto
        retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
        """
        result = self.db.query(Admin_model).all()
        return result

    def get_admin_filter(self, fliters: admin_filter_schema):
        """
        esta funcion trear todos los  registro de la base de datos de  admin segun el criterio en que este se filtre ,
        con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
        seguridad ya que los admin tienen varios permisos, luego de valiadar, si el token no es correcto
        retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
        """
        if fliters.fullname != None:
            result = self.db.query(Admin_model).filter(
                Admin_model.fullname == fliters.fullname).all()
            return result
        elif fliters.id != None:
            result = self.db.query(Admin_model).filter(
                Admin_model.id == fliters.id).all()
            return result

        elif fliters.document_number != None:
            result = self.db.query(Admin_model).filter(
                Admin_model.document_number == fliters.document_number).all()
            return result
        elif fliters.email != None:
            result = self.db.query(Admin_model).filter(
                Admin_model.email == fliters.email).all()
            return result
        elif fliters.city != None:
            result = self.db.query(Admin_model).filter(
                Admin_model.city == fliters.city).all()
            return result
        elif fliters.job_title != None:
            result = self.db.query(Admin_model).filter(
                Admin_model.job_title == fliters.job_title).all()
            return result

    def create_Admin(self, admin: Admin_schema):
        """
        esta funcion trear todos los  registro de la base de datos de  admin,
        con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
        seguridad ya que los admins tienen varios permisos, luego de valiadar, si el token no es correcto
        retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
        """
        hash_password = bcrypt.hashpw(
            admin.password.encode(), bcrypt.gensalt())
        admin.password = hash_password
        new_admin = Admin_model(**admin.dict())
        self.db.add(new_admin)
        self.db.commit()
        return JSONResponse(content={"mensage": "el usuario se ha registrado"})

    def Admin_updates(self, email: str, data: Admin_update):
        """
        esta funcion actualiza un registro de tipo admin utilizando el archivo en el paquete de schema,
        con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
        seguridad ya que los admins tienen varios permisos, luego de valiadar, si el token no es correcto
        retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
        """
        admin = self.db.query(Admin_model).filter(
            Admin_model.email == email).first()
        admin.email = data.email
        admin.first_number = data.first_number
        admin.city = data.city
        hash_password = bcrypt.hashpw(
            data.password.encode(), bcrypt.gensalt())
        data.password = hash_password
        admin.password = data.password
        admin.job_title = data.job_title
        self.db.commit()
        return

    def delete_admin(self, email: str):
        """
        esta funcion eliminar un registro de tipo admin,
        con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
        seguridad ya que los admins tienen varios permisos, luego de valiadar, si el token no es correcto
        retorna un error, pero si si, verifica los datos y sin son validos retornara que el usuario ha sido eliminado
        """
        self.db.query(Admin_model).filter(
            Admin_model.email == email).delete()
        self.db.commit()
        return

    def verificate_admin(self, login_schema_sign_up: login_schema_sign_up):
        """
        esta funcion es para verificar si  registro  es de tipo admin,
        con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
        seguridad ya que los admins tienen varios permisos, luego de valiadar, si el token no es correcto

        retorna un error, pero si si, verifica los datos y sin son validos retornara que el usuario ha sido eliminado
        """
        result = self.db.query(Admin_model).filter(
            Admin_model.document_number == login_schema_sign_up.document_number).first()
        if result is None:
            return None

        if bcrypt.checkpw(login_schema_sign_up.password.encode(), result.password) and result.document_type == login_schema_sign_up.document_type:
            return result
        else:
            return None

    def validate_admin(self, email: str):
        result = self.db.query(Admin_model).filter(
            Admin_model.email == email).first()
        if result is None:
            return None
        else:
            return result
