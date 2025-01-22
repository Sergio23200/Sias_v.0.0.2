from schemas.Medications_schema_base import Medications_schema, Medications_update, Medications_user, medicatios_filter_schema
from models.Medications import Medications_model
from fastapi.responses import JSONResponse


class Medications_service():
    def __init__(self, db) -> None:
        self.db = db

    def get_medications_filter(self, valor: medicatios_filter_schema):
        """
        esta funcion trear todos los  registro de la base de datos de  afiliado, segun el criterio en que este se filtre ,
        con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
        seguridad ya que los afiliados tienen varios permisos, luego de valiadar, si el token no es correcto
        retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
        """
        if valor.id != None:
            result = self.db.query(Medications_model).filter(
                Medications_model.id == valor.id).all()
            return result
        elif valor.generic_name != None:
            result = self.db.query(Medications_model).filter(
                Medications_model.generic_name == valor.generic_name).all()
            return result
        elif valor.price != None:
            result = self.db.query(Medications_model).filter(
                Medications_model.price == valor.price).all()
            return result

    def get_medications(self):
        """
        esta funcion trear todos los  registro de la base de datos de  medications,
        con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
        seguridad ya que los admins tienen varios permisos, luego de valiadar, si el token no es correcto
        retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
        """
        result = self.db.query(Medications_model).all()
        return result

    def create_medications(self, medications: Medications_schema):
        """
        esta funcion crea un registro de tipo medications utilizando el archivo en el paquete de schema,
        con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
        seguridad ya que los afiliados  tienen varios permisos, luego de valiadar, si el token no es correcto
        retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
        """
        new_medications = Medications_model(**medications.dict())
        self.db.add(new_medications)
        self.db.commit()
        return

    def update_medications(self, generic_name: str, data: Medications_update):
        """
        esta funcion actualiza un registro de tipo medications utilizando el archivo en el paquete de schema,
        con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
        seguridad ya que los admins tienen varios permisos, luego de valiadar, si el token no es correcto
        retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
        """
        medications = self.db.query(Medications_model).filter(
            Medications_model.generic_name == generic_name).first()
        medications.dose = data.dose
        medications.price = data.price
        medications.contraindications = data.contraindications
        medications.aviable = data.aviable
        medications.Stocks = data.Stocks
        self.db.commit()
        return

    def delete_medications(self, generic_name: str):
        """
        esta funcion eliminar un registro de tipo medications,
        con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
        seguridad ya que los admins tienen varios permisos, luego de valiadar, si el token no es correcto
        retorna un error, pero si si, verifica los datos y sin son validos retornara que el usuario ha sido eliminado
        """
        self.db.query(Medications_model).filter(
            Medications_model.document_number == generic_name).delete()
        self.db.commit()
        return

    def user_medications(self, generic_name: str, query: Medications_user):
        """
        esta funcion actualiza un registro de tipo medications utilizando el archivo en el paquete de schema,
        con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
        seguridad ya que los admins tienen varios permisos, luego de valiadar, si el token no es correcto
        retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
        """

        medication = self.db.query(Medications_model).filter(
            Medications_model.generic_name == generic_name).first()

        if not medication:
            return JSONResponse(content={"message": "El medicamento no existe"}, status_code=404)

        if medication.Stocks < query.Stocks:
            return JSONResponse(content={"message": "No hay suficiente inventario para esta solicitud"}, status_code=400)

        if query.user_money < medication.price:
            return JSONResponse(content={"message": "El dinero no es suficiente para esta solicitud"}, status_code=400)

        medication.Stocks -= query.Stocks
        query.user_money -= medication.price

        self.db.commit()

        return JSONResponse(content={"message": "se guardo el medicamento para ti"}, status_code=400)
