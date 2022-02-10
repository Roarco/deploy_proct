
from flask import Blueprint, render_template, request, redirect, url_for, flash
from services.Students import studentsService
from services.TypeId import typeIdService

Estudiante = Blueprint("Estudiante", __name__)


@Estudiante.route("/home_student")
def home_Student():
    return render_template("home_student.html")


@Estudiante.route("/students")
def crud_Student():
    typeids = typeIdService().get_typeIds()
    students = studentsService().get_students()
    return render_template("crud_student.html", typeids=typeids, students=students)


@Estudiante.route("/new_student", methods=["POST"])
def new_Student():
    codigo_Student = request.form["codigo_Student"]
    name = request.form["name"]
    lastname = request.form["lastname"]
    id_typeid = int(request.form["id_typeid"])
    IDNumber = request.form["IDNumber"]

    #consultamos si ese estudiante ya existe
    students = studentsService().get_student(codigo_Student)
    if students:
        flash("Este estudiante ya existe")
        return redirect(url_for("Estudiante.crud_Student"))

    new_student = studentsService.create_student(
        codigo_Student, name, lastname, id_typeid, IDNumber
    )
    typeids = typeIdService().get_typeIds()
    students = studentsService().get_students()
    return render_template("crud_student.html", students=students, typeids=typeids)


@Estudiante.route("/update_student/<id>" , methods=["GET", "POST"])
def update_Student(id):
        idviejo = id
        studennt = studentsService().get_student(idviejo)
        if request.method == "GET":
            typeids = typeIdService().get_typeIds()
            return render_template("update_student.html", student=studennt, typeids=typeids)

        if request.method == "POST":
            name = request.form["name"]
            lastname = request.form["lastname"]
            id_typeid = int(request.form["id_typeid"])
            IDNumber = request.form["IDNumber"]


            updated_student = studentsService.update_student(
                idviejo, name, lastname, id_typeid, IDNumber
            )
            return redirect(url_for("Estudiante.crud_Student"))


@Estudiante.route("/delete_student/<id>")
def delete_Student(id):
    student = studentsService.delete_student(id)

    return redirect(url_for("Estudiante.crud_Student"))