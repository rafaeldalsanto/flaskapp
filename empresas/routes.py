from flask import request, jsonify

from empresas import empresas_blueprint
from empresas.servicos import obter_empresas, inserir_empresa


@empresas_blueprint.route('/empresas', methods=('GET',))
def listar_empresas():
    empresas = obter_empresas()
    return jsonify(empresas)


@empresas_blueprint.route('/empresas', methods=('POST',))
def criar_empresa():
    parametros = request.get_json()
    empresa = inserir_empresa(
        nome=parametros['nome']
    )
    return jsonify(empresa)
