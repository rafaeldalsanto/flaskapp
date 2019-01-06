import weakref
from functools import wraps


def merge_dicts(base, other):
    return dict(base, **other) if other is not None else base


def memoize(fn):
    cache = weakref.WeakKeyDictionary()

    @wraps(fn)
    def wrap(self):
        if self in cache:
            return cache[self]
        value = cache[self] = fn(self)
        return value

    return wrap
