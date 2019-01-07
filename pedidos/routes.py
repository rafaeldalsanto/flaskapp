from flask import request, jsonify

from pedidos import pedidos_blueprint
from pedidos.servicos import obter_pedidos


@pedidos_blueprint.route('/<int:empresa_id>/pedidos', methods=('GET',))
def listar_pedidos(empresa_id):
    pedidos = obter_pedidos(empresa_id=empresa_id)
    return jsonify(pedidos)


@pedidos_blueprint.route('/<int:empresa_id>/pedidos', methods=('POST',))
def criar_novo_pedido(empresa_id):
    parametros = request.get_json()

    return jsonify(parametros)


@pedidos_blueprint.route('/<int:empresa_id>/pedidos', methods=('PUT',))
def alterar_pedido(empresa_id):
    parametros = request.get_json()

    return jsonify(parametros)
