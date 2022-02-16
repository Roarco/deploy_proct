from models.models import Documents
from utils.db import db

class documentService:

    def __init__(self):
        pass

    def get_documents(self):
        documents = Documents.query.all()
        db.session.commit()
        return documents

    def get_document_cod_student(codigo_Student):
        document = Documents.query.filter_by(codigo_Student=codigo_Student).order_by(Documents.id.desc()).all()
        db.session.commit()
        return document
    def get_document_id(id):
        document = Documents.query.filter_by(id=id).first()
        db.session.commit()
        return document

    def create_document(codigo_Student, datetime_document, id_state, student_observation, administrative_code, administrative_observation):
        new_document = Documents(codigo_Student, datetime_document, id_state, student_observation, administrative_code, administrative_observation)
        db.session.add(new_document)
        db.session.commit()
        return "Document created"

    def update_document(id,datetime_document,id_state,administrative_code, administrative_observation):
        document = documentService.get_document_id(id)
        document.datetime_document = datetime_document
        document.id_state = id_state
        document.administrative_code = administrative_code
        document.administrative_observation = administrative_observation
        db.session.commit()
        return "Document updated"

    def delete_document(codigo_Student):
        document = Documents.query.filter_by(codigo_Student=codigo_Student).first()
        db.session.delete(document)
        db.session.commit()
        return "Document deleted"