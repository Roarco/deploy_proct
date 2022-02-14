from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models.auth import auth
from models.models import Student, Administrative
from utils.db import db
from services.Documents import documentService
from services.TypeId import typeIdService

auths = Blueprint("auths", __name__)


@auths.route("/")
def index():
    return render_template("layout_login.html")


@auths.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        code = request.form["code"]
        IDNumber = request.form["IDNumber"]
        type_of_user = int(request.form["type_of_user"])
        session["code"] = code
        session["type_of_user"] = type_of_user

        if type_of_user == 1:
            student = Student.query.filter_by(codigo_Student=code).first()

            if student is None:
                flash(
                    "Usuario no encontrado por favor comuniquese con el administrador"
                )
                return redirect(url_for("auths.login"))
            elif student.IDNumber != IDNumber or student.codigo_Student != code:
                flash("Credenciales incorrectas")
                return redirect(url_for("auths.login"))
            else:
                return redirect(url_for("Estudiante.home_Student"))
        elif type_of_user == 2:
            administrative = Administrative.query.filter_by(
                administrative_code=code
            ).first()

            if administrative is None:
                flash(
                    "Usuario no encontrado por favor comuniquese con el administrador de la pagina"
                )
                return redirect(url_for("auths.login"))
            elif administrative.IDNumber != IDNumber:
                flash("Credenciales incorrectas")
                return redirect(url_for("auths.login"))
            else:
                return redirect(
                    url_for(
                        "Administrativo.home_administrativo"
                    )
                )
    if request.method == "GET":
        return redirect(url_for("auths.index"))

@auths.route("/logout")
def logout():
    session.pop("code", None)
    return redirect(url_for("auths.login"))
