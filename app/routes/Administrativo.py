from flask import Blueprint, render_template, request, redirect, url_for, flash
from services.TypeId import typeIdService
from services.Documents import documentService

Administrativo = Blueprint('Administrativo', __name__)

@Administrativo.route('/home_administrativo')
def home_administrativo():
    typeids = typeIdService().get_typeIds()
    alldocuments = documentService().get_documents()
    return render_template('home_administrative.html', typeids=typeids, documents=alldocuments)