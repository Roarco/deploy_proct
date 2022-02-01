from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.auth import auth
from models.Students import Student
from utils.db import db

auths = Blueprint("auths", __name__)

@auths.route("/" , methods=["GET", "POST"])
def login():
    if request.method == "POST":
        codigo_Student = request.form["codigo_Student"]
        IDNumber = request.form["IDNumber"]
        type_of_user = int(request.form["type_of_user"])

        if type_of_user == 1:
            student = Student.query.filter_by(codigo_Student=codigo_Student).first()

            if student is None:
                flash("Usuario no encontrado por favor comuniquese con el administrador")
                return redirect(url_for("auths.login"))
            elif student.IDNumber != IDNumber or student.codigo_Student != codigo_Student:
                flash("Credenciales incorrectas")
                return redirect(url_for("auths.login"))
            else:
                return redirect(url_for("students.home_Student"))
        elif type_of_user == 2:
            pass

    if request.method == "GET":
        return render_template("layout_login.html")
