from schemas.Ips_schema import Ips_schema, Ips_update
from models.Ips import Ips_model


class ips_service():
    def __init__(self, db) -> None:
        self.db = db

    def get_ips(self):
        result = self.db.query(Ips_model).all()
        return result

    def create_ips(self, ips: Ips_schema):
        new_ips = Ips_model(**ips.dict())
        self.db.add(new_ips)
        self.db.commit()
        return

    def update_ips(self, name_hospital: int, data: Ips_update):
        ips = self.db.query(Ips_model).filter(
            Ips_model.name_hospital == name_hospital).first()
        ips.email = data.email
        ips.phone_number = data.phone_number
        self.db.commit()
        return

    def delete_ips(self, name_ips: str):
        self.db.query(Ips_model).filter(
            Ips_model.name_ips == name_ips).delete()
        self.db.commit()
        return
