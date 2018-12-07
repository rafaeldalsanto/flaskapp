from flask import request, jsonify

from pedidos import pedidos_blueprint
from pedidos.gateways import filtrar_pedidos


@pedidos_blueprint.route('/pedidos', methods=('GET',))
def listar_pedidos():
    pedidos = filtrar_pedidos()
    return jsonify(pedidos)


@pedidos_blueprint.route('/pedidos', methods=('POST',))
def cadastrar_pedido():
    parametros = request.get_json()

    return jsonify(parametros)


@pedidos_blueprint.route('/pedidos', methods=('PUT',))
def alterar_pedido():
    parametros = request.get_json()

    return jsonify(parametros)
