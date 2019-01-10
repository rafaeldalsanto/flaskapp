from sqlalchemy import inspect


def as_list_of_dicts(objs):
    return [as_dict(obj) for obj in objs]


def as_dict(obj):
    return {c.key: getattr(obj, c.key) for c in inspect(obj).mapper.column_attrs}


def columns(table, names):
    column_attrs = inspect(table).mapper.column_attrs
    return [column_attrs[name].expression for name in names]
