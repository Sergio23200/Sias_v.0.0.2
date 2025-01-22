from schemas.Ips_schema import Ips_schema, Ips_update, ips_filter_schema
from models.Ips import Ips_model


class ips_service():
    def __init__(self, db) -> None:
        self.db = db

    def get_ips(self):
        """
        esta funcion trear todos los  registro de la base de datos de  ips
        con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
        seguridad ya que los admin tienen varios permisos, luego de valiadar, si el token no es correcto
        retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
        """
        result = self.db.query(Ips_model).all()
        return result

    def get_ips_filter(self, valor: ips_filter_schema):
        """
        esta funcion trear todos los  registro de la base de datos de  afiliado, segun el criterio en que este se filtre ,
        con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
        seguridad ya que los afiliados tienen varios permisos, luego de valiadar, si el token no es correcto
        retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
        """
        if valor.id != None:
            result = self.db.query(Ips_model).filter(
                Ips_model.id == valor.id).all()
            return result
        elif valor.name_hospital != None:
            result = self.db.query(Ips_model).filter(
                Ips_model.name_hospital == valor.name_hospital).all()
            return result
        elif valor.city != None:
            result = self.db.query(Ips_model).filter(
                Ips_model.city == valor.city).all()
            return result
        elif valor.Address != None:
            result = self.db.query(Ips_model).filter(
                Ips_model.Address == valor.Address).all()
            return result
        elif valor.email != None:
            result = self.db.query(Ips_model).filter(
                Ips_model.email == valor.email).all()
            return result
        elif valor.phone_number != None:
            result = self.db.query(Ips_model).filter(
                Ips_model.phone_number == valor.phone_number).all()
            return result

    def create_ips(self, ips: Ips_schema):
        """
        esta funcion crea un registro de tipo ips utilizando el archivo en el paquete de schema,
        con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
        seguridad ya que los admins tienen varios permisos, luego de valiadar, si el token no es correcto
        retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
        """
        new_ips = Ips_model(**ips.dict())
        self.db.add(new_ips)
        self.db.commit()
        return

    def update_ips(self, name_hospital: int, data: Ips_update):
        """
        esta funcion actualiza un registro de tipo admin utilizando el archivo en el paquete de schema,
        con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
        seguridad ya que los admins tienen varios permisos, luego de valiadar, si el token no es correcto
        retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
        """
        ips = self.db.query(Ips_model).filter(
            Ips_model.name_hospital == name_hospital).first()
        ips.email = data.email
        ips.phone_number = data.phone_number
        self.db.commit()
        return

    def delete_ips(self, name_ips: str):
        """
        esta funcion eliminar un registro de tipo ips,
        con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
        seguridad ya que los admins tienen varios permisos, luego de valiadar, si el token no es correcto
        retorna un error, pero si si, verifica los datos y sin son validos retornara que el usuario ha sido eliminado
        """
        self.db.query(Ips_model).filter(
            Ips_model.name_ips == name_ips).delete()
        self.db.commit()
        return
