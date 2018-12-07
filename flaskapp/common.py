def merge_dicts(base, other):
    return dict(base, **other) if other is not None else base
