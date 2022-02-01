from flask import Blueprint, render_template, request, redirect, url_for, flash

Administrativo = Blueprint('Administrativo', __name__)

@Administrativo.route('/home_administrativo')
def home_administrativo():
    return "Hola Administrativo"