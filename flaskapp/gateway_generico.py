from flaskapp.extensions import db
from datetime import datetime
from flaskapp.sqlalchemy_utils import as_dict, filter_or_exclude
from flaskapp.common import merge_dicts


def inserir(tabela, **fields):
    props = merge_dicts({
        'data_de_criacao': datetime.now(),
        'ultima_alteracao': datetime.now(),
    }, fields)

    obj = tabela(**props)
    db.session.add(obj)
    db.session.flush()

    return as_dict(obj)


def atualizar(tabela, id, **fields):
    props = merge_dicts({
        'ultima_alteracao': datetime.now(),
    }, fields)

    if 'data_de_criacao' in props:
        del props['data_de_criacao']

    db.session.query(tabela) \
        .filter(tabela.id == id) \
        .update(props)


def filtrar(tabela, **filtros):
    query = db.session.query(tabela)
    rows = []
    for row in filter_or_exclude(query, negate=False, **filtros).all():
        rows.append(as_dict(row))
    return rows


def obter_por_id(tabela, id):
    registros = filtrar(tabela, id=id)

    if len(registros) == 0:
        return None

    return registros[0]
