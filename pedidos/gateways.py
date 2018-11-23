def as_dict(obj):
    from sqlalchemy import inspect

    return {c.key: getattr(obj, c.key) for c in inspect(obj).mapper.column_attrs}


def merge_dicts(base, other):
    return dict(base, **other) if other is not None else base


def inserir(model, **kwargs):
    from flaskapp import db
    from datetime import datetime

    props = merge_dicts({
        'data_de_criacao': datetime.now(),
        'ultima_alteracao': datetime.now(),
    }, kwargs)

    obj = model(**props)
    db.session.add(obj)
    db.session.flush()

    return as_dict(obj)


def atualizar(model, model_id, **kwargs):
    from flaskapp import db
    from datetime import datetime

    props = merge_dicts({
        'ultima_alteracao': datetime.now(),
    }, kwargs)

    if 'data_de_criacao' in props:
        del props['data_de_criacao']

    db.session.query(model) \
        .filter(model.id == model_id) \
        .update(props)


def inserir_pedido(**kwargs):
    from pedidos.models import Pedido

    return inserir(Pedido, **kwargs)


def atualizar_pedido(pedido_id, **kwargs):
    from pedidos.models import Pedido

    atualizar(Pedido, pedido_id, **kwargs)
