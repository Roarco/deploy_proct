
from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models.models import Student
from services.Students import studentsService
from services.TypeId import typeIdService
from services.Documents import documentService

Estudiante = Blueprint("Estudiante", __name__)


@Estudiante.route("/home_student")
def home_Student():
    if "code" in session:
        if session["type_of_user"] == 1:
            code = session["code"]
            student = Student.query.filter_by(codigo_Student=code).first()
            documents = documentService.get_document_cod_student(code)
            if documents == []:
                document = []
            else:
                document = documents[0]
            return render_template(
                "home_student.html", student=student, document=document
            )
        else:
            return redirect(url_for("auths.index"))
    else:
        return redirect(url_for("auths.index"))



@Estudiante.route("/students")
def crud_Student():
    if "code" in session:
        if session["type_of_user"] == 2:
            typeids = typeIdService().get_typeIds()
            students = studentsService().get_students()
            return render_template("crud_student.html", typeids=typeids, students=students)
        else:
            return redirect(url_for("auths.index"))
    else:
        return redirect(url_for("auths.index"))


@Estudiante.route("/new_student", methods=["POST"])
def new_Student():
    if "code" in session:
        if session["type_of_user"] == 2:
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
            else:
                studentsService.create_student(
                    codigo_Student, name, lastname, id_typeid, IDNumber
                )
            typeids = typeIdService().get_typeIds()
            students = studentsService().get_students()
            return render_template("crud_student.html", students=students, typeids=typeids)
        else:
            return redirect(url_for("auths.index"))
    else:
        return redirect(url_for("auths.index"))


@Estudiante.route("/update_student/<id>" , methods=["GET", "POST"])
def update_Student(id):
    if "code" in session:
        if session["type_of_user"] == 2:
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
                studentsService.update_student(
                idviejo, name, lastname, id_typeid, IDNumber
            )
            return redirect(url_for("Estudiante.crud_Student"))
        else:
            return redirect(url_for("auths.index"))
    else:
        return redirect(url_for("auths.index"))


@Estudiante.route("/delete_student/<id>")
def delete_Student(id):
    if "code" in session:
        if session["type_of_user"] == 2:
            studentsService.delete_student(id)
            return redirect(url_for("Estudiante.crud_Student"))
        else:
            return redirect(url_for("auths.index"))
    else:
        return redirect(url_for("auths.index"))