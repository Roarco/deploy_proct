
from models.models import Administrative
from utils.db import db

class AdministrativeService:
    def __init__(self):
        pass

    def get_administrative(self, administrative_code):
        administrative = Administrative.query.filter_by(administrative_code=administrative_code).first()
        db.session.commit()
        return administrative

    def get_administrative_all(self):
        administratives = Administrative.query.all()
        db.session.commit()
        return administratives

    def create_administrative(self, administrative_code, name, lastname, id_typeid, IDNumber):
        new_administrative = Administrative(administrative_code, name, lastname, id_typeid, IDNumber)
        db.session.add(new_administrative)
        db.session.commit()
        return "Administrative created"

    def update_administrative(self, administrative_code, name, lastname, id_typeid, IDNumber):
        administrative = Administrative.query.filter_by(administrative_code=administrative_code).first()
        administrative.name = name
        administrative.lastname = lastname
        administrative.id_typeid = id_typeid
        administrative.IDNumber = IDNumber
        db.session.commit()
        return "Administrative updated"

    def delete_administrative(self, administrative_code):
        administrative = Administrative.query.filter_by(administrative_code=administrative_code).first()
        db.session.delete(administrative)
        db.session.commit()
        return "Administrative deleted"