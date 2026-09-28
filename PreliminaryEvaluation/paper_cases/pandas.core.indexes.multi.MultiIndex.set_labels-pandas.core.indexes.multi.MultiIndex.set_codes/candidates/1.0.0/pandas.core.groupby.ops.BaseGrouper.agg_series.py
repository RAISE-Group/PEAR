def agg_series(self, obj: Series, func):
    assert self.ngroups != 0
    if len(obj) == 0:
        return self._aggregate_series_pure_python(obj, func)
    elif is_extension_array_dtype(obj.dtype):
        return self._aggregate_series_pure_python(obj, func)
    elif obj.index._has_complex_internals:
        return self._aggregate_series_pure_python(obj, func)
    try:
        return self._aggregate_series_fast(obj, func)
    except ValueError as err:
        if 'Function does not reduce' in str(err):
            pass
        else:
            raise
    return self._aggregate_series_pure_python(obj, func)