from utils.db import db

# Create a class for the table Students
class Student(db.Model):
    __tablename__ = "Students"

    # Define the columns of the table
    codigo_Student = db.Column(db.String(15), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    id_typeid = db.Column(db.Integer, db.ForeignKey("typeId.id"), nullable=False)
    TypeId = db.relationship("typeId", backref=db.backref("typeId", lazy=True))
    IDNumber = db.Column(db.String(15), nullable=False)

    def __init__(self, codigo_Student, name, lastname, id_typeid, IDNumber):
        self.codigo_Student = codigo_Student
        self.name = name
        self.lastname = lastname
        self.id_typeid = id_typeid
        self.IDNumber = IDNumber


# create a class for the table TypeId
class typeId(db.Model):
    __tablename__ = "typeId"

    # Define the columns of the table
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(100), nullable=False)

    def __init__(self, description):
        self.description = description

# create a class for the table Administrative
class Administrative(db.Model):
    __tablename__ = "Administrative"

    # Define the columns of the table
    administrative_code = db.Column(db.String(15), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    id_typeid = db.Column(db.Integer, db.ForeignKey("typeId.id"), nullable=False)
    TypeId = db.relationship("typeId", backref=db.backref("typeId_Adm", lazy=True))
    IDNumber = db.Column(db.String(15), nullable=False)

    def __init__(self, administrative_code, name, lastname, id_typeid, IDNumber):
        self.administrative_code = administrative_code
        self.name = name
        self.lastname = lastname
        self.id_typeid = id_typeid
        self.IDNumber = IDNumber
