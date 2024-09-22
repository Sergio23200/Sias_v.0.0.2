from schemas.Medications_schema import Medications_schema, Medications_update
from models.Medications import Medications_model


class Medications_service():
    def __init__(self, db) -> None:
        self.db = db

    def get_medications(self):
        result = self.db.query(Medications_model).all()
        return result

    def create_medications(self, medications: Medications_schema):
        new_medications = Medications_model(**medications.dict())
        self.db.add(new_medications)
        self.db.commit()
        return

    def update_medications(self, generic_name: str, data: Medications_update):
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
        self.db.query(Medications_model).filter(
            Medications_model.document_number == generic_name).delete()
        self.db.commit()
        return
