from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.Students import Student
from utils.db import db

students = Blueprint("students", __name__)


@students.route("/home_student")
def home_Student():
    return render_template("home_student.html")


@students.route("/new_student", methods=["POST"])
def new_Student():
    codigo_Student = request.form["codigo_Student"]
    name = request.form["name"]
    lastname = request.form["lastname"]
    IDType = request.form["IDType"]
    IDNumber = request.form["IDNumber"]

    new_student = Student(codigo_Student, name, lastname, IDType, IDNumber)
    db.session.add(new_student)
    db.session.commit()
    return "Student created"


@students.route("/update_student")
def update_Student():
    return "Has actualizado un Student"


@students.route("/delete_student")
def delete_Student():
    return "Has eliminado un Student"
