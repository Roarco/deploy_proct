
from models.models import Student
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

    def delete_student(self, codigo_Student):
        student = Student.query.filter_by(codigo_Student=codigo_Student).first()
        db.session.delete(student)
        db.session.commit()
        return "Student deleted"