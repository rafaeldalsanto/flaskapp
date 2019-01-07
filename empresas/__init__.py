from flask import Blueprint
empresas_blueprint = Blueprint('empresas', __name__, template_folder='templates')

from empresas import routes

