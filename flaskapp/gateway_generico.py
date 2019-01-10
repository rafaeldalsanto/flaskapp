from datetime import datetime

from flaskapp.common import merge_dicts
from flaskapp.extensions import db
from flaskapp.sqlalchemy_utils import as_dict


class Transaction:
    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val is None:
            db.session.commit()
        else:
            db.session.rollback()


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


def obter(tabela, **filtros):
    query = db.session.query(tabela).filter_by(**filtros)
    return list(query)


def obter_um(tabela, **filtros):
    registros = obter(tabela, **filtros)

    if len(registros) == 0:
        return None

    return registros[0]
