from schemas.admin_schema import Admin_schema, Admin_update
import bcrypt
from models.Admin import Admin_model


class Admin_service():
    def __init__(self, db) -> None:
        self.db = db

    def get_admin(self):
        result = self.db.query(Admin_model).all()
        return result

    def get_admin(self):
        result = self.db.query(Admin_model).all()
        return result

    def create_Admin(self, admin: Admin_schema):
        hash_password = bcrypt.hashpw(
            admin.password.encode(), bcrypt.gensalt())
        admin.password = hash_password
        new_admin = Admin_model(**admin.dict())
        self.db.add(new_admin)
        self.db.commit()
        return

    def Admin_updates(self, document_number: int, data: Admin_update):
        admin = self.db.query(Admin_model).filter(
            Admin_model.document_number == document_number).first()
        admin.email = data.email
        admin.first_number = data.first_number
        admin.city = data.city
        hash_password = bcrypt.hashpw(
            data.password.encode(), bcrypt.gensalt())
        data.password = hash_password
        admin.password = data.password
        admin.job_title = data.job_title
        self.db.commit()
        return

    def delete_admin(self, document_number: int):
        self.db.query(Admin_model).filter(
            Admin_model.document_number == document_number).delete()
        self.db.commit()
        return

    def verificate_admin(self, email: str, password: str):
        result = self.db.query(Admin_model).filter(
            Admin_model.email == email).first()
        if result is None:
            return None

        if bcrypt.checkpw(password.encode(), result.password):
            return result
        else:
            return None

    def validate_admin(self, email: str):
        result = self.db.query(Admin_model).filter(
            Admin_model.email == email).first()
        if result is None:
            return None
        else:
            return None
