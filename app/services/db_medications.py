from models.base_medicamento_user import base_medications_model
from schemas.medications_user_schema import Medications_user_filter_schema, Medications_user_schema


class Medications_service():
    def __init__(self, db) -> None:
        self.db = db

    def get_medications(self):
        """
        esta funcion trear todos los  registro de la base de datos de  medications,
        con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
        seguridad ya que los admins tienen varios permisos, luego de valiadar, si el token no es correcto
        retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
        """
        result = self.db.query(base_medications_model).all()
        return result

    def get_medications_appoinment(self, valor: Medications_user_filter_schema):
        """
        esta funcion trear todos los  registro de la base de datos de  afiliado, segun el criterio en que este se filtre ,
        con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
        seguridad ya que los afiliados tienen varios permisos, luego de valiadar, si el token no es correcto
        retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
        """
        if valor.id != "":
            result = self.db.query(base_medications_model), filter(
                base_medications_model.id == valor)
            return result
        elif valor.generic_name != "":
            result = self.db.query(base_medications_model), filter(
                base_medications_model.generic_name == valor)
            return result
        elif valor.fullname_user != "":
            result = self.db.query(base_medications_model), filter(
                base_medications_model.fullname_user == valor)
            return result

    def create_medications_appoinment(self, appointment: Medications_user_schema):
        """
        esta funcion crea un registro de tipo medications utilizando el archivo en el paquete de schema,
        con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
        seguridad ya que los afiliados  tienen varios permisos, luego de valiadar, si el token no es correcto
        retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
        """
        new_medications = base_medications_model(**appointment.dict())
        self.db.add(new_medications)
        self.db.commit()
        return
