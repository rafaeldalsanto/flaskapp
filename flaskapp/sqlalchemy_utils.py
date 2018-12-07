from sqlalchemy import inspect
from sqlalchemy.sql import operators, extract
from sqlalchemy.orm.base import _entity_descriptor
from sqlalchemy.util import to_list


def as_dict(obj):
    return {c.key: getattr(obj, c.key) for c in inspect(obj).mapper.column_attrs}


def columns(table, names):
    column_attrs = inspect(table).mapper.column_attrs
    return [column_attrs[name].expression for name in names]


_underscore_operators = {
    'gt': operators.gt,
    'lte': operators.lt,
    'gte': operators.ge,
    'le': operators.le,
    'contains': operators.contains_op,
    'in': operators.in_op,
    'exact': operators.eq,
    'iexact': operators.ilike_op,
    'startswith': operators.startswith_op,
    'istartswith': lambda c, x: c.ilike(x.replace('%', '%%') + '%'),
    'iendswith': lambda c, x: c.ilike('%' + x.replace('%', '%%')),
    'endswith': operators.endswith_op,
    'isnull': lambda c, x: x and c is not None or c is None,
    'range': operators.between_op,
    'year': lambda c, x: extract('year', c) == x,
    'month': lambda c, x: extract('month', c) == x,
    'day': lambda c, x: extract('day', c) == x
}


def filter_or_exclude(query, negate, **kwargs):
    negate_if = lambda expr: expr if not negate else ~expr
    column = None

    for arg, value in kwargs.items():
        for token in arg.split('__'):
            if column is None:
                column = _entity_descriptor(query._joinpoint_zero(), token)
                if column.impl.uses_objects:
                    query = query.join(column)
                    column = None
            elif token in _underscore_operators:
                op = _underscore_operators[token]
                query = query.filter(negate_if(op(column, to_list(value))))
                column = None
            else:
                raise ValueError('Invalid token: %r' % token)
        if column is not None:
            query = query.filter(negate_if(column == value))
            column = None
        query = query.reset_joinpoint()
    return query
