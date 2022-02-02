
# from utils.db import db


# class Student(db.Model):
#     codigo_Student = db.Column(db.String(15), primary_key=True)
#     name = db.Column(db.String(50), nullable=False)
#     lastname = db.Column(db.String(50), nullable=False)
#     IDType = db.Column(db.Integer, db.ForeignKey('typeId.id'), nullable=False)
#     TypeId = db.relationship('typeId', backref=db.backref('typeId', lazy=True))
#     IDNumber = db.Column(db.String(15), nullable=False)

#     def __init__(self, codigo_Student, name, lastname, IDType, IDNumber):
#         self.codigo_Student = codigo_Student
#         self.name = name
#         self.lastname = lastname
#         self.IDType = IDType
#         self.IDNumber = IDNumber


