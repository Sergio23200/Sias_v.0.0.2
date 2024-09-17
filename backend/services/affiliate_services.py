from schemas.affiliate_schema import Affiliate_schema
import bcrypt
from models.Affilate import Affiliate_model


class Affiliate_service():
    def __init__(self, db) -> None:
        self.db = db

    def get_afiliate(self):
        result = self.db.query(Affiliate_model).all()
        return result

    def get_affiliates_filter(self, document_number):
        result = self.db.query(Affiliate_model).filter(
            Affiliate_model.document_number == document_number)
        return result

    def create_Affiliate(self, affiliate: Affiliate_schema):
        hash_password = bcrypt.hashpw(
            affiliate.password.encode(), bcrypt.gensalt())
        affiliate.password = hash_password
        new_affiliate = Affiliate_model(**affiliate.dict())
        self.db.add(new_affiliate)
        self.db.commit()
        return

    def Affiliate_update(self, document_number: int, data: Affiliate_schema):
        affiliate = self.db.query(Affiliate_model).filter(
            Affiliate_model.document_number == document_number).first()
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

    def delete_affilate(self, document_number: int):
        self.db.query(Affiliate_model).filter(
            Affiliate_model.document_number == document_number).delete()
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
            return None
