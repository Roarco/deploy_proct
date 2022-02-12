from importlib.resources import path
import os
import webbrowser
import datetime
from flask import Blueprint, render_template, request, redirect, url_for, flash
from services.Documents import documentService
from services.TypeId import typeIdService
from services.States import stateService
from services.Administrativo import AdministrativeService
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
        elif len(documents) > 0 and documents[0].id_state == 2:
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

#ruta para la previsualizacion del documento
@Documents.route("/preview/<id>", methods=["GET", "POST"])
def preview(id):
    ruta = os.path.join(app.files, f"{id} .pdf")
    webbrowser.open(ruta)
    return redirect(url_for("Administrativo.home_administrativo"))



#ruta para verificar documento por estudiante
@Documents.route("/verify/<id>", methods=["GET", "POST"])
def verify(id):
    data = eval(id)
    documents = documentService().get_documents()
    document_by_student = documentService.get_document_cod_student(data[0])
    typeids = typeIdService().get_typeIds()
    administrative = AdministrativeService().get_administrative(data[1])
    states = stateService().get_states()
    return render_template('home_administrative.html', documents=documents, document_by_student=document_by_student[0], typeids=typeids,administrative=administrative,states=states)

#ruta para revisar documento
@Documents.route("/revision/<id>,<id_adm>", methods=["GET", "POST"])
def revision(id,id_adm):
    adm = AdministrativeService().get_administrative(id_adm)
    document_by_student = documentService.get_document_cod_student(id)
    states = stateService().get_states()
    return render_template('revision_document.html', document=document_by_student[0],states=states, adm=adm)

#ruta para actualizar documento
@Documents.route("/update/<id>", methods=["POST"])
def update(id):
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
        typeids = typeIdService().get_typeIds()
        alldocuments = documentService().get_documents()
        administrative = AdministrativeService().get_administrative(administrative_code)
        print(administrative)
        return render_template('home_administrative.html', typeids=typeids, documents=alldocuments, administrative=administrative)