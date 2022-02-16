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

# Create a class for the table states
class State(db.Model):
    __tablename__ = "State"

    # Define the columns of the table
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(100), nullable=False)

    def __init__(self, description):
        self.description = description

# Create a class for the table documents
class Documents(db.Model):
    __tablename__ = "Documents"

    # Define the columns of the table
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    codigo_Student = db.Column(db.String(15), db.ForeignKey("Students.codigo_Student"), nullable=False)
    student = db.relationship("Student", backref=db.backref("student_document", lazy=True))
    datetime_document = db.Column(db.DateTime, nullable=False)
    id_state = db.Column(db.Integer, db.ForeignKey("State.id"), nullable=False)
    State = db.relationship("State", backref=db.backref("state_document", lazy=True))
    student_observation = db.Column(db.String(100), nullable=True)
    administrative_code = db.Column(db.String(15), db.ForeignKey("Administrative.administrative_code"), nullable=True)
    administrative_observation = db.Column(db.String(100), nullable=True)
    administrative = db.relationship("Administrative", backref=db.backref("administrative_revision", lazy=True))


    def __init__(self, codigo_Student, datetime_document, id_state, student_observation, administrative_code, administrative_observation):
        self.codigo_Student = codigo_Student
        self.datetime_document = datetime_document
        self.id_state = id_state
        self.student_observation = student_observation
        self.administrative_code = administrative_code
        self.administrative_observation = administrative_observation


