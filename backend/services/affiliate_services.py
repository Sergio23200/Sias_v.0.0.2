from schemas.affiliate_schema import Affiliate_schema, affilate_update, filter_afiliate_schema
import bcrypt
from models.Affilate import Affiliate_model


class Affiliate_service():
    def __init__(self, db) -> None:
        self.db = db

    def get_afiliate(self):
        """
        esta funcion trear todos los  registro de la base de datos de  afiliado
        con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
        seguridad ya que los afiliados tienen varios permisos, luego de valiadar, si el token no es correcto
        retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
        """

        result = self.db.query(Affiliate_model).all()
        return result

    def get_affiliates_filter(self, valor: filter_afiliate_schema):
        """
        esta funcion trear todos los  registro de la base de datos de  afiliado, segun el criterio en que este se filtre ,
        con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
        seguridad ya que los afiliados tienen varios permisos, luego de valiadar, si el token no es correcto
        retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
        """
        if valor.fullname != "":
            result = self.db.query(Affiliate_model), filter(
                Affiliate_model.fullname == valor)
            return result
        elif valor-id != "":
            result = self.db.query(Affiliate_model), filter(
                Affiliate_model.id == valor)
            return result
        elif valor.document_number != "":
            result = self.db.query(Affiliate_model), filter(
                Affiliate_model.document_number == valor)
            return result
        elif valor.email != "":
            result = self.db.query(Affiliate_model), filter(
                Affiliate_model.email == valor)
            return result
        elif valor.city != "":
            result = self.db.query(Affiliate_model), filter(
                Affiliate_model.city == valor)
            return result
        elif valor.Clinical_history != "":
            result = self.db.query(Affiliate_model), filter(
                Affiliate_model.Clinical_history == valor)
            return result

    def create_Affiliate(self, affiliate: Affiliate_schema):
        """
        esta funcion crea un registro de tipo afiliado utilizando el archivo en el paquete de schema,
        con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
        seguridad ya que los afiliados  tienen varios permisos, luego de valiadar, si el token no es correcto
        retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
        """

        hash_password = bcrypt.hashpw(
            affiliate.password.encode(), bcrypt.gensalt())
        affiliate.password = hash_password
        new_affiliate = Affiliate_model(**affiliate.dict())
        self.db.add(new_affiliate)
        self.db.commit()
        return

    def Affiliate_update(self, id: int, data: affilate_update):
        """        
        esta funcion actualiza un registro de tipo afiliadoutilizando el archivo en el paquete de schema,
        con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
        seguridad ya que los afiliado tienen varios permisos, luego de valiadar, si el token no es correcto
        retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado        
        """
        affiliate = self.db.query(Affiliate_model).filter(
            Affiliate_model.id == id).first()
        affiliate.email = data.email
        affiliate.Address = data.Address
        affiliate.phone_number = data.phone_number
        affiliate.city = data.city
        hash_password = bcrypt.hashpw(
            data.password.encode(), bcrypt.gensalt())
        data.password = hash_password
        affiliate.password = data.password
        affiliate.membership_type = data.membership_type
        self.db.commit()
        return

    def delete_affilate(self, id: int):
        """
        esta funcion eliminar un registro de tipo admin,
        con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
        seguridad ya que los admins tienen varios permisos, luego de valiadar, si el token no es correcto
        retorna un error, pero si si, verifica los datos y sin son validos retornara que el usuario ha sido eliminado
        """
        self.db.query(Affiliate_model).filter(
            Affiliate_model.id == id).delete()
        self.db.commit()
        return

    def vericate_afilate(self, email: str, password: str):
        result = self.db.query(Affiliate_model).filter(
            Affiliate_model.email == email).first()
        if result is None:
            return None

        if bcrypt.checkpw(password.encode(), result.password):
            return result
        else:
            return None

    def validate_affilate(self, email: str):
        result = self.db.query(Affiliate_model).filter(
            Affiliate_model.email == email).first()
        if result is None:
            return None
        else:
            return result["email"]
