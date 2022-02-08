import os
import app
from models.models import Student
from services.Documents import documentService
from utils.db import db


class studentsService:
    def __init__(self):
        pass

    def get_students(self):
        return Student.query.all()

    def get_student(self, codigo_Student):
        return Student.query.filter_by(codigo_Student=codigo_Student).first()

    def create_student(codigo_Student, name, lastname, id_typeid, IDNumber):
        new_student = Student(codigo_Student, name, lastname, id_typeid, IDNumber)
        db.session.add(new_student)
        db.session.commit()
        return "Student created"

    def update_student(self, codigo_Student, name, lastname, IDType, IDNumber):
        student = Student.query.filter_by(codigo_Student=codigo_Student).first()
        student.name = name
        student.lastname = lastname
        student.IDType = IDType
        student.IDNumber = IDNumber
        db.session.commit()
        return "Student updated"

    def delete_student(codigo_Student):
        document_student = documentService.get_document_cod_student(codigo_Student)
        if len(document_student) > 0:
            documentService.delete_document(codigo_Student)
            os.remove(os.path.join(app.files, f"{codigo_Student} .pdf"))

        student = Student.query.filter_by(codigo_Student=codigo_Student).first()
        db.session.delete(student)
        db.session.commit()
        return "Student deleted"
