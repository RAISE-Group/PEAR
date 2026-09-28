@classmethod
def _simple_new(cls, values, name=None, dtype=None):
    result = object.__new__(cls)
    result._data = values
    result._index_data = values
    result._name = name
    result._calls = 0
    return result._reset_identity()