from models.models import Documents
from utils.db import db

class documentService:

    def __init__(self):
        pass

    def get_documents(self):
        return Documents.query.all()

    def get_document_cod_student(codigo_Student):
        return Documents.query.filter_by(codigo_Student=codigo_Student).all()

    def create_document(codigo_Student, datetime_document, id_state, student_observation, administrative_code, administrative_observation):
        new_document = Documents(codigo_Student, datetime_document, id_state, student_observation, administrative_code, administrative_observation)
        db.session.add(new_document)
        db.session.commit()
        return "Document created"

    def update_document(self, codigo_Student, datetime_document, id_state, student_observation, administrative_code, administrative_observation):
        document = Documents.query.filter_by(codigo_Student=codigo_Student).first()
        document.datetime_document = datetime_document
        document.id_state = id_state
        document.student_observation = student_observation
        document.administrative_code = administrative_code
        document.administrative_observation = administrative_observation
        db.session.commit()
        return "Document updated"