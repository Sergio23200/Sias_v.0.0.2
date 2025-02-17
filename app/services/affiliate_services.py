from schemas.affiliate_schema import Affiliate_schema, affilate_update, filter_afiliate_schema
from fastapi.responses import JSONResponse
from fastapi import HTTPException
import bcrypt
from models.Affilate import Affiliate_model
from schemas.login_schema import login_schema_sign_up


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
        if valor.id != None:
            result = self.db.query(Affiliate_model).filter(
                Affiliate_model.id == valor.id).all()
            return result
        elif valor.document_number != None:
            result = self.db.query(Affiliate_model).filter(
                Affiliate_model.document_number == valor.document_number).all()
            return result
        elif valor.email != None:
            result = self.db.query(Affiliate_model).filter(
                Affiliate_model.email == valor.email).all()
            return result
        elif valor.city != None:
            result = self.db.query(Affiliate_model).filter(
                Affiliate_model.city == valor.city).all()
            return result
        elif valor.Clinical_history != None:
            result = self.db.query(Affiliate_model).filter(
                Affiliate_model.Clinical_history == valor.Clinical_history).all()
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

    def return_date(self, email: str):
        result = self.db.query(Affiliate_model).filter(
            Affiliate_model.email == email).first()
        return result

    def verificate_doc(self, document_number: int):
        result = self.db.query(Affiliate_model).filter(
            Affiliate_model.document_number == document_number).first()
        return result

    def vericate_afilate(self, login_schema_sign_up: login_schema_sign_up):
        result = self.db.query(Affiliate_model).filter(
            Affiliate_model.document_number == login_schema_sign_up.document_number).first()
        if result is None:

            return None

        if bcrypt.checkpw(login_schema_sign_up.password.encode(), result.password) and result.document_type == login_schema_sign_up.document_type:
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

    def validate_affilate_email(self, email: str):
        result = self.db.query(Affiliate_model).filter(
            Affiliate_model.email == email).first()
        if result is None:
            return None
        else:
            return result
