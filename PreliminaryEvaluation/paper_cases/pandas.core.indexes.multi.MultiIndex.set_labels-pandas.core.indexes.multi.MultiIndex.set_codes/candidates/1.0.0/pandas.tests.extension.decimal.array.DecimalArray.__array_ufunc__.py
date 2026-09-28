def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
    if not all((isinstance(t, self._HANDLED_TYPES + (DecimalArray,)) for t in inputs)):
        return NotImplemented
    inputs = tuple((x._data if isinstance(x, DecimalArray) else x for x in inputs))
    result = getattr(ufunc, method)(*inputs, **kwargs)

    def reconstruct(x):
        if isinstance(x, (decimal.Decimal, numbers.Number)):
            return x
        else:
            return DecimalArray._from_sequence(x)
    if isinstance(result, tuple):
        return tuple((reconstruct(x) for x in result))
    else:
        return reconstruct(result)