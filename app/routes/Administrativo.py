from flask import Blueprint, render_template, redirect, url_for, session
from services.TypeId import typeIdService
from services.Documents import documentService
from services.Administrativo import AdministrativeService

Administrativo = Blueprint('Administrativo', __name__)

@Administrativo.route('/home_administrativo',)
def home_administrativo():
    if "code" in session:
        if session["type_of_user"] == 2:
            code = session["code"]
            administrative = AdministrativeService().get_administrative(code)
            typeids = typeIdService().get_typeIds()
            alldocuments = documentService().get_documents()
            return render_template("home_administrative.html",administrative=administrative,typeids=typeids, documents=alldocuments)
        else:
            return redirect(url_for("auths.index"))
    else:
        return redirect(url_for("auths.index"))