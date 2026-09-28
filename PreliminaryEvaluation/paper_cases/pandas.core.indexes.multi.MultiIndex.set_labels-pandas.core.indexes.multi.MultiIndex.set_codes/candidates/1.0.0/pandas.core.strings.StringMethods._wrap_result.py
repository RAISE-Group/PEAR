def _wrap_result(self, result, use_codes=True, name=None, expand=None, fill_value=np.nan, returns_string=True):
    from pandas import Index, Series, MultiIndex
    if use_codes and self._is_categorical:
        result = take_1d(result, Series(self._orig, copy=False).cat.codes, fill_value=fill_value)
    if not hasattr(result, 'ndim') or not hasattr(result, 'dtype'):
        return result
    assert result.ndim < 3
    if self._is_string and returns_string:
        dtype = 'string'
    else:
        dtype = None
    if expand is None:
        expand = result.ndim != 1
    elif expand is True and (not isinstance(self._orig, ABCIndexClass)):

        def cons_row(x):
            if is_list_like(x):
                return x
            else:
                return [x]
        result = [cons_row(x) for x in result]
        if result:
            max_len = max((len(x) for x in result))
            result = [x * max_len if len(x) == 0 or x[0] is np.nan else x for x in result]
    if not isinstance(expand, bool):
        raise ValueError('expand must be True or False')
    if expand is False:
        if name is None:
            name = getattr(result, 'name', None)
        if name is None:
            name = self._orig.name
    if isinstance(self._orig, ABCIndexClass):
        if is_bool_dtype(result):
            return result
        if expand:
            result = list(result)
            out = MultiIndex.from_tuples(result, names=name)
            if out.nlevels == 1:
                out = out.get_level_values(0)
            return out
        else:
            return Index(result, name=name)
    else:
        index = self._orig.index
        if expand:
            cons = self._orig._constructor_expanddim
            result = cons(result, columns=name, index=index, dtype=dtype)
        else:
            cons = self._orig._constructor
            result = cons(result, name=name, index=index, dtype=dtype)
        return result