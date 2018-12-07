from flask import Blueprint
geral_blueprint = Blueprint('geral', __name__, template_folder='templates')

from geral import routes
