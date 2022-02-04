# from flask import Blueprint, render_template, request, redirect, url_for, flash
# from services.Documents import documentService


# documents = Blueprint("documents", __name__)

# @documents.route("/" , methods=["GET"])
# def home_documents():
#     documents = documentService.get_documents()
#     return documents

# @documents.route("/code_student" , methods=["GET"])
# def get_documents_cod_student(cod_student):
#     document = documentService.get_document_cod_student(cod_student)
#     return document