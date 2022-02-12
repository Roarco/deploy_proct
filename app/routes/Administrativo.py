from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models.models import Student, Administrative
from services.TypeId import typeIdService
from services.Documents import documentService

Administrativo = Blueprint('Administrativo', __name__)

@Administrativo.route('/home_administrativo',)
def home_administrativo():
    if "code" in session:
        code = session["code"]
        administrative = Administrative.query.filter_by(administrative_code=code).first()
        typeids = typeIdService().get_typeIds()
        alldocuments = documentService().get_documents()
        return render_template("home_administrative.html",administrative=administrative,typeids=typeids, documents=alldocuments)
    else:
        return redirect(url_for("auths.index"))