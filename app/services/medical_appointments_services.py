from schemas.Medical_appointment_schema import medical_appointments_schema, fliter_appoinments_schema, update_appoinments_schema
from models.Medical_appointments import Medical_appointments_model
from services.affiliate_services import Affiliate_service
from models.Affilate import Affiliate_model


class appoinments_service():
    def __init__(self, db) -> None:
        self.db = db

    def get_appoinment(self):
        """
        esta funcion trear todos los  registro de la base de datos de  appoinment,
        con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por
        seguridad ya que los admins tienen varios permisos, luego de valiadar, si el token no es correcto
        retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
        """
        result = self.db.query(Medical_appointments_model).all()
        return result

    def get_appoinments_filter(self, valor: fliter_appoinments_schema):
        """
        esta funcion trear todos los  registro de la base de datos de  citas, segun el criterio en que este se filtre ,
        con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por
        seguridad ya que los citas tienen varios permisos, luego de valiadar, si el token no es correcto
        retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
        """
        if valor.id != None:
            result = self.db.query(Medical_appointments_model).filter(
                Medical_appointments_model.id == valor.id).all()
            return result
        elif valor.document_number_affiliate != None:
            result = self.db.query(Medical_appointments_model).filter(
                Medical_appointments_model.generic_name == valor.document_number_affiliate)
            return result
        elif valor.name_doctor != None:
            result = self.db.query(Medical_appointments_model).filter(
                Medical_appointments_model.name_doctor == valor.name_doctor).all()
            return result
        elif valor.day != None:
            result = self.db.query(Medical_appointments_model).filter(
                Medical_appointments_model.day == valor.day).all()
            return result
        elif valor.hospital_name != None:
            result = self.db.query(Medical_appointments_model), filter(
                Medical_appointments_model.hospital_name == valor.hospital_name).all()
            return result
        elif valor.hour != None:
            result = self.db.query(Medical_appointments_model).filter(
                Medical_appointments_model.hour == valor.hour).all()
            return result

    def create_appoinments(self, appointment: medical_appointments_schema):
        """
        esta funcion crea un registro de tipo citas utilizando el archivo en el paquete de schema,
        con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
        seguridad ya que los afiliados  tienen varios permisos, luego de valiadar, si el token no es correcto
        retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado
        """
        new_appoinment = Medical_appointments_model(**appointment.dict())

        self.db.add(new_appoinment)
        self.db.commit()
        return

    def appoinments_update(self, id: int, data: update_appoinments_schema):
        """        
        esta funcion actualiza un registro de tipo appoinments utilizando el archivo en el paquete de schema,
        con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
        seguridad ya que los afiliado tienen varios permisos, luego de valiadar, si el token no es correcto
        retorna un error, pero si si, verifica los datos y sin son validos retornara  que el usuario ha sido eliminado        
        """
        appoinments = self.db.query(Medical_appointments_model).filter(
            Medical_appointments_model.id == id).first()
        appoinments.name_doctor = data.name_doctor
        appoinments.hour = data.hour
        appoinments.day = data.day
        appoinments.city = data.city
        self.db.commit()
        return

    def delete_appoinments(self, id: int):
        """
        esta funcion eliminar un registro de tipo admin,
        con este busca tambien si el usuario esta autenticado antes de hacer el proceso, esto por 
        seguridad ya que los admins tienen varios permisos, luego de valiadar, si el token no es correcto
        retorna un error, pero si si, verifica los datos y sin son validos retornara que el usuario ha sido eliminado
        """
        self.db.query(Medical_appointments_model).filter(
            Medical_appointments_model.id == id).delete()
        self.db.commit()
        return
