from schemas.hospital_chema import Hospital_schema, Hospital_update
from models.Hospital import Hospital_model


class hospìtal_service():
    def __init__(self, db) -> None:
        self.db = db

    def get_hospital(self):
        result = self.db.query(Hospital_model).all()
        return result

    def create_hospital(self, ips: Hospital_schema):
        new_hospital = Hospital_model(**ips.dict())
        self.db.add(new_hospital)
        self.db.commit()
        return

    def update_hospital(self, name_hospital: int, data: Hospital_update):
        hospital = self.db.query(Hospital_model).filter(
            Hospital_model.name_hospital == name_hospital).first()
        hospital.email = data.email
        hospital.phone_number = data.phone_number
        hospital.ambulance_dispo = data.ambulance_dispo
        hospital.ambulances_on_route = data.ambulances_on_route
        self.db.commit()
        return

    def delete_hospital(self, name_hospital: str):
        self.db.query(Hospital_model).filter(
            Hospital_model.name_hospital == name_hospital).delete()
        self.db.commit()
        return
