from flask import Blueprint, render_template, request, redirect, url_for, flash
from services.Students import studentsService
from services.TypeId import typeIdService

Estudiante = Blueprint("Estudiante", __name__)


@Estudiante.route("/home_student")
def home_Student():
    return render_template("home_student.html")

@Estudiante.route("/crud_student")
def crud_Student():
      typeids = typeIdService().get_typeIds()
      students = studentsService().get_students()
      print(students)
      return render_template("crud_student.html", typeids=typeids , students=students)



@Estudiante.route("/new_student", methods=["POST"])
def new_Student():
    codigo_Student = request.form["codigo_Student"]
    name = request.form["name"]
    lastname = request.form["lastname"]
    id_typeid = int(request.form["id_typeid"])
    IDNumber = request.form["IDNumber"]

    new_student = studentsService.create_student(
        codigo_Student, name, lastname, id_typeid, IDNumber
    )
    typeids = typeIdService().get_typeIds()
    students = studentsService().get_students()
    return render_template("crud_student.html", students=students, typeids=typeids)


@Estudiante.route("/update_student")
def update_Student():
    return "Has actualizado un Student"


@Estudiante.route("/delete_student")
def delete_Student():
    return "Has eliminado un Student"
