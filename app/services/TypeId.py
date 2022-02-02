from models.models import typeId
from utils.db import db


class typeIdService:
    def __init__(self):
        pass

    def get_typeIds(self):
        return typeId.query.all()

    def get_typeId(id):
        return typeId.query.filter_by(id=id).first()

    def create_typeId(self, description):
        typeid = typeId(description=description)
        db.session.add(typeid)
        db.session.commit()
        return "TypeId created"

    def update_typeId(self, id, description):
        typeid = typeId.query.filter_by(id=id).first()
        typeid.description = description
        db.session.commit()
        return "TypeId updated"

    def delete_typeId(id):
        typeid = typeId.query.filter_by(id=id).first()
        db.session.delete(typeid)
        db.session.commit()
        return "TypeId deleted"
