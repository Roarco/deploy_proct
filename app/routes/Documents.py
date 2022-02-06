import os
import datetime
from flask import Blueprint, render_template, request, redirect, url_for, flash
from services.Documents import documentService
import app


Documents = Blueprint("documents", __name__)


@Documents.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        codigo_Student = request.form["codigo_Student"]
        datetime_document = datetime.datetime.now()
        id_state = 1
        student_observation = request.form["observacion"]
        administrative_code = None
        administrative_observation = None
        file = request.files["file"]
        documents = documentService.get_document_cod_student(codigo_Student)
        if len(documents) == 0:
            file.save(os.path.join(app.files, f"{codigo_Student} .pdf"))
            new_document = documentService.create_document(
                codigo_Student,
                datetime_document,
                id_state,
                student_observation,
                administrative_code,
                administrative_observation,
            )
            documents = documentService.get_document_cod_student(codigo_Student)
            for i in documents:
                student = i.student
            document = documents[0]
            return render_template("home_student.html",student=student,document=document)
        elif len(documents) > 0 and documents.pop().id_state == 2:
            file.save(os.path.join(app.files, f"{codigo_Student} .pdf"))
            new_document = documentService.create_document(
                codigo_Student,
                datetime_document,
                id_state,
                student_observation,
                administrative_code,
                administrative_observation,
            )
            documents = documentService.get_document_cod_student(codigo_Student)
            for i in documents:
                student = i.student
            document= documents[0]
            return render_template("home_student.html",student=student,document=document)
        else:
            flash("El estudiante ya tiene un documento en proceso")
            documents = documentService.get_document_cod_student(codigo_Student)
            for i in documents:
                student = i.student
            document= documents[0]
            return render_template("home_student.html",student=student,document=document)

    return redirect(url_for("Estudiante.home_student"))
