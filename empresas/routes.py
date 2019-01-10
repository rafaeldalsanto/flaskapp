from flask import request, jsonify

from empresas import empresas_blueprint
from empresas.servicos import obter_empresas, inserir_empresa
from flaskapp.gateway_generico import Transaction
from flaskapp.sqlalchemy_utils import as_list_of_dicts


@empresas_blueprint.route('/empresas', methods=('GET',))
def listar_empresas():
    empresas = obter_empresas()
    return jsonify(as_list_of_dicts(empresas))


@empresas_blueprint.route('/empresas', methods=('POST',))
def criar_empresa():
    parametros = request.get_json()

    with Transaction():
        empresa = inserir_empresa(
            nome=parametros['nome']
        )
    return jsonify(empresa)
