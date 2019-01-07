from sqlalchemy import func

from flaskapp.extensions import db
from flaskapp.gateway_generico import inserir, atualizar, obter, obter_um
from flaskapp.models import Pedido


def inserir_pedido(**campos):
    return inserir(Pedido, **campos)


def atualizar_pedido(pedido_id, **campos):
    atualizar(Pedido, pedido_id, **campos)


def obter_pedidos(**filtros):
    return obter(Pedido, **filtros)


def obter_um_pedido(**filtros):
    return obter_um(Pedido, **filtros)


def obter_numero_do_proximo_pedido(empresa_id):
    ultimo_numero = db.session \
        .query(func.coalesce(func.max(Pedido.numero), 0)) \
        .filter_by(empresa_id=empresa_id) \
        .scalar()

    return ultimo_numero + 1
