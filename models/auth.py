from utils.db import db

class auth(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codigo_Student = db.Column(db.String(15), nullable=False)
    IDNumber = db.Column(db.String(15), nullable=False)

    def __init__(self, codigo_Student, IDNumber):
        self.codigo_Student = codigo_Student
        self.IDNumber = IDNumber