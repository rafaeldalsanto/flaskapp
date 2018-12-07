from flaskapp.gateway_generico import inserir, atualizar, filtrar, obter_por_id
from pedidos.models import Pedido


def inserir_pedido(**campos):
    return inserir(Pedido, **campos)


def atualizar_pedido(pedido_id, **campos):
    atualizar(Pedido, pedido_id, **campos)


def filtrar_pedidos(**filtros):
    return filtrar(Pedido, **filtros)


def obter_pedido_por_id(pedido_id):
    return obter_por_id(Pedido, pedido_id)
