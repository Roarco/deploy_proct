
import os
import webbrowser
import datetime
from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from services.Documents import documentService
from services.TypeId import typeIdService
from services.States import stateService
from services.Administrativo import AdministrativeService
from werkzeug.utils import secure_filename

import index

Documents = Blueprint("documents", __name__)


@Documents.route("/upload", methods=["GET", "POST"])
def upload():
    if "code" in session:
        if session["type_of_user"] == 1:
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
                    file.save(os.path.join(index.files, f"{codigo_Student} .pdf"))
                    documentService.create_document(
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
                elif len(documents) > 0 and documents[0].id_state == 2:
                    file.save(os.path.join(index.files, f"{codigo_Student} .pdf"))
                    documentService.create_document(
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
            if request.method == "GET":
                return redirect(url_for("Estudiante.home_student"))
        else:
            return redirect(url_for("auths.index"))
    else:
        return redirect(url_for("auths.index"))

#ruta para la previsualizacion del documento
@Documents.route("/preview/<id>", methods=["GET", "POST"])
def preview(id):
    if "code" in session:
        if session["type_of_user"] == 2:
            ruta = os.path.join(index.files, f"{id} .pdf")
            webbrowser.open(ruta)
            return redirect(url_for("Administrativo.home_administrativo"))
        else:
            return redirect(url_for("auths.index"))
    else:
        return redirect(url_for("auths.index"))



#ruta para verificar documento por estudiante
@Documents.route("/verify/<id>", methods=["GET", "POST"])
def verify(id):
    if "code" in session:
        if session["type_of_user"] == 2:
            data = eval(id)
            documents = documentService().get_documents()
            document_by_student = documentService.get_document_cod_student(data[0])
            typeids = typeIdService().get_typeIds()
            administrative = AdministrativeService().get_administrative(data[1])
            states = stateService().get_states()
            return render_template('home_administrative.html', documents=documents, document_by_student=document_by_student[0], typeids=typeids,administrative=administrative,states=states)
        else:
            return redirect(url_for("auths.index"))
    else:
        return redirect(url_for("auths.index"))

#ruta para actualizar estado del documento
@Documents.route("/update/<id>", methods=["POST"])
def update(id):
    if "code" in session:
        if session["type_of_user"] == 2:
            id = id
            document = documentService.get_document_id(id)

            if document:
                datetime_document = datetime.datetime.now()
                id_state = request.form["id_state"]
                administrative_code = request.form["administrative_code"]
                aministrative_observation = request.form["aministrative_observation"]

                documentService.update_document(
                    id,
                    datetime_document,
                    id_state,
                    administrative_code,
                    aministrative_observation,
                )
                return redirect(url_for("Administrativo.home_administrativo"))
            else:
                return redirect(url_for("Administrativo.home_administrativo"))
        else:
            return redirect(url_for("auths.index"))
    else:
        return redirect(url_for("auths.index"))