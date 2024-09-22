from schemas.Specialist_schemas import Specialist_schema, Specialist_update
from models.Specialist import Specialist_model


class specialist_service():
    def __init__(self, db) -> None:
        self.db = db

    def get_specialist(self):
        result = self.db.query(Specialist_model).all()
        return result

    def create_specialist(self, specialist: Specialist_schema):
        new_specialist = Specialist_model(**specialist.dict())
        self.db.add(new_specialist)
        self.db.commit()
        return

    def update_specialist(self, document_number: int, data: Specialist_update):
        Specialist = self.db.query(Specialist_model).filter(
            Specialist_model.number_document == document_number).first()
        Specialist.email = data.email
        Specialist.phone_number = data.phone_number
        Specialist.specialty = data.specialty
        self.db.commit()
        return

    def delete_specialist(self, document_number: int):
        self.db.query(Specialist_model).filter(
            Specialist_model.document_number == document_number).delete()
        self.db.commit()
        return
