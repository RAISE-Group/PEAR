def get_result(self, obj, method, key, axis):
    """ return the result for this obj with this key and this axis """
    if isinstance(key, dict):
        key = key[axis]
    if method == 'indexer':
        method = 'ix'
        key = obj._get_axis(axis)[key]
    with catch_warnings(record=True):
        try:
            xp = getattr(obj, method).__getitem__(_axify(obj, key, axis))
        except AttributeError:
            xp = getattr(obj, method).__getitem__(key)
    return xp