def __setitem__(self, key, value):
    msg = 'SparseArray does not support item assignment via setitem'
    raise TypeError(msg)