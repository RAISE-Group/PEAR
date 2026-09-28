@cache_readonly
def _engine(self):
    _ndarray_values = self._ndarray_values
    return self._engine_type(lambda: _ndarray_values, len(self))