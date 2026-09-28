@classmethod
def _scalar_data_error(cls, data):
    return TypeError(f'{cls.__name__}(...) must be called with a collection of some kind, {repr(data)} was passed')