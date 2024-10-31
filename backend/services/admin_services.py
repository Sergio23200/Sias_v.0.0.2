from schemas.admin_schema import Admin_schema, Admin_update, admin_filter_schema
import bcrypt
from models.Admin import Admin_model


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

    def get_admin_filter(self, valor: admin_filter_schema):
        """
        esta funcion trear todos los  registro de la base de datos de  admin segun el criterio en que este se filtre ,
        con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
        seguridad ya que los admin tienen varios permisos, luego de valiadar, si el token no es correcto
        retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
        """
        if valor.fullname != "":
            result = self.db.query(Admin_model), filter(
                Admin_model.fullname == valor)
            return result
        elif valor-id != "":
            result = self.db.query(Admin_model), filter(
                Admin_model.id == valor)
            return result

        elif valor.document_number != "":
            result = self.db.query(Admin_model), filter(
                Admin_model.document_number == valor)
            return result
        elif valor.email != "":
            result = self.db.query(Admin_model), filter(
                Admin_model.email == valor)
            return result
        elif valor.city != "":
            result = self.db.query(Admin_model), filter(
                Admin_model.city == valor)
            return result
        elif valor.job_title != "":
            result = self.db.query(Admin_model), filter(
                Admin_model.job_title == valor)
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
        return

    def Admin_updates(self, document_number: int, data: Admin_update):
        """
        esta funcion actualiza un registro de tipo admin utilizando el archivo en el paquete de schema,
        con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
        seguridad ya que los admins tienen varios permisos, luego de valiadar, si el token no es correcto
        retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
        """
        admin = self.db.query(Admin_model).filter(
            Admin_model.document_number == document_number).first()
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

    def delete_admin(self, document_number: int):
        """
        esta funcion eliminar un registro de tipo admin,
        con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
        seguridad ya que los admins tienen varios permisos, luego de valiadar, si el token no es correcto
        retorna un error, pero si si, verifica los datos y sin son validos retornara que el usuario ha sido eliminado
        """
        self.db.query(Admin_model).filter(
            Admin_model.document_number == document_number).delete()
        self.db.commit()
        return

    def verificate_admin(self, email: str, password: str):
        """
        esta funcion es para verificar si  registro  es de tipo admin,
        con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
        seguridad ya que los admins tienen varios permisos, luego de valiadar, si el token no es correcto
        retorna un error, pero si si, verifica los datos y sin son validos retornara que el usuario ha sido eliminado
        """
        result = self.db.query(Admin_model).filter(
            Admin_model.email == email).first()
        if result is None:
            return None

        if bcrypt.checkpw(password.encode(), result.password):
            return result
        else:
            return None

    def validate_admin(self, email: str):
        result = self.db.query(Admin_model).filter(
            Admin_model.email == email).first()
        if result is None:
            return None
        else:
            return result.email
