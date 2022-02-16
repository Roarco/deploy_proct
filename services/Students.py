import os
import index
from models.models import Student
from services.Documents import documentService
from utils.db import db


class studentsService:
    def __init__(self):
        pass

    def get_students(self):
        students = Student.query.all()
        db.session.commit()
        return students

    def get_student(self,codigo_Student):
        student = Student.query.filter_by(codigo_Student=codigo_Student).first()
        db.session.commit()
        return student

    def create_student(codigo_Student, name, lastname, id_typeid, IDNumber):
        new_student = Student(codigo_Student, name, lastname, id_typeid, IDNumber)
        db.session.add(new_student)
        db.session.commit()
        return "Student created"

    def update_student(idviej, name, lastname, id_typeid, IDNumber):
        student = Student.query.filter_by(codigo_Student=idviej).first()
        student.name = name
        student.lastname = lastname
        student.id_typeid = id_typeid
        student.IDNumber = IDNumber
        db.session.commit()
        return "Student updated"

    def delete_student(codigo_Student):
        document_student = documentService.get_document_cod_student(codigo_Student)
        if len(document_student) > 0:
            documentService.delete_document(codigo_Student)
            os.remove(os.path.join(index.files, f"{codigo_Student} .pdf"))

        student = Student.query.filter_by(codigo_Student=codigo_Student).first()
        db.session.delete(student)
        db.session.commit()
        return "Student deleted"
