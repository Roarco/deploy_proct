from flask import Blueprint, render_template, request, redirect, url_for, flash
from services.Students import studentsService

students = Blueprint("students", __name__)


@students.route("/home_student")
def home_Student():
    return render_template("home_student.html")


@students.route("/new_student", methods=["POST"])
def new_Student():
    codigo_Student = request.form["codigo_Student"]
    name = request.form["name"]
    lastname = request.form["lastname"]
    id_typeid = int(request.form["id_typeid"])
    IDNumber = request.form["IDNumber"]

    new_student = studentsService.create_student(
        codigo_Student, name, lastname, id_typeid, IDNumber
    )
    return new_student


@students.route("/update_student")
def update_Student():
    return "Has actualizado un Student"


@students.route("/delete_student")
def delete_Student():
    return "Has eliminado un Student"
