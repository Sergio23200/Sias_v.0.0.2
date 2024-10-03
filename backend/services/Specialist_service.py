from schemas.Specialist_schemas import Specialist_schema, Specialist_update
from models.Specialist import Specialist_model


class specialist_service():
    def __init__(self, db) -> None:
        self.db = db

    def get_specialist(self):
        """
        esta funcion trear todos los  registro de la base de datos de  especialista,
        con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
        seguridad ya que los admins tienen varios permisos, luego de valiadar, si el token no es correcto
        retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
        """
        result = self.db.query(Specialist_model).all()
        return result

    def create_specialist(self, specialist: Specialist_schema):
        """
        esta funcion crea un registro de tipo espicialista utilizando el archivo en el paquete de schema,
        con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
        seguridad ya que los afiliados  tienen varios permisos, luego de valiadar, si el token no es correcto
        retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
        """
        new_specialist = Specialist_model(**specialist.dict())
        self.db.add(new_specialist)
        self.db.commit()
        return

    def update_specialist(self, document_number: int, data: Specialist_update):
        """
        esta funcion actualiza un registro de tipo especialista utilizando el archivo en el paquete de schema,
        con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
        seguridad ya que los admins tienen varios permisos, luego de valiadar, si el token no es correcto
        retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
        """
        Specialist = self.db.query(Specialist_model).filter(
            Specialist_model.number_document == document_number).first()
        Specialist.email = data.email
        Specialist.phone_number = data.phone_number
        Specialist.specialty = data.specialty
        self.db.commit()
        return

    def delete_specialist(self, document_number: int):
        """
        esta funcion eliminar un registro de tipo medications,
        con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
        seguridad ya que los admins tienen varios permisos, luego de valiadar, si el token no es correcto
        retorna un error, pero si si, verifica los datos y sin son validos retornara que el usuario ha sido eliminado
        """
        self.db.query(Specialist_model).filter(
            Specialist_model.document_number == document_number).delete()
        self.db.commit()
        return
