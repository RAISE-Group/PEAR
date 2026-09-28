def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
    out = kwargs.get('out', ())
    for x in inputs + out:
        if not isinstance(x, self._HANDLED_TYPES + (PandasArray,)):
            return NotImplemented
    inputs = tuple((x._ndarray if isinstance(x, PandasArray) else x for x in inputs))
    if out:
        kwargs['out'] = tuple((x._ndarray if isinstance(x, PandasArray) else x for x in out))
    result = getattr(ufunc, method)(*inputs, **kwargs)
    if type(result) is tuple and len(result):
        if not lib.is_scalar(result[0]):
            return tuple((type(self)(x) for x in result))
        else:
            return result
    elif method == 'at':
        return None
    else:
        if not lib.is_scalar(result):
            result = type(self)(result)
        return result