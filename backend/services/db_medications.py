from models.base_medicamento_user import base_medications_model


class Medications_service():
    def __init__(self, db) -> None:
        self.db = db

    def get_medications(self):
        result = self.db.query(base_medications_model).all()
        return result

    def create_medications_appoinment(self, appointment: dict):
        new_medications = base_medications_model(**appointment.dict())
        self.db.add(new_medications)
        self.db.commit()
        return
