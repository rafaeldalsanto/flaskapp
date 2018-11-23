from flask import Blueprint
pedidos_blueprint = Blueprint('pedidos', __name__, template_folder='templates')

from . import routes
from . import models
