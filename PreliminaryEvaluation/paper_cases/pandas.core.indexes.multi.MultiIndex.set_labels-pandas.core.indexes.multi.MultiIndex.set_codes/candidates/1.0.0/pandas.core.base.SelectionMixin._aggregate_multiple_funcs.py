def _aggregate_multiple_funcs(self, arg, _axis):
    from pandas.core.reshape.concat import concat
    if _axis != 0:
        raise NotImplementedError('axis other than 0 is not supported')
    if self._selected_obj.ndim == 1:
        obj = self._selected_obj
    else:
        obj = self._obj_with_exclusions
    results = []
    keys = []
    if obj.ndim == 1:
        for a in arg:
            colg = self._gotitem(obj.name, ndim=1, subset=obj)
            try:
                new_res = colg.aggregate(a)
            except TypeError:
                pass
            else:
                results.append(new_res)
                name = com.get_callable_name(a) or a
                keys.append(name)
    else:
        for index, col in enumerate(obj):
            colg = self._gotitem(col, ndim=1, subset=obj.iloc[:, index])
            try:
                new_res = colg.aggregate(arg)
            except (TypeError, DataError):
                pass
            except ValueError as err:
                if 'Must produce aggregated value' in str(err):
                    pass
                elif 'no results' in str(err):
                    pass
                else:
                    raise
            else:
                results.append(new_res)
                keys.append(col)
    if not len(results):
        raise ValueError('no results')
    try:
        return concat(results, keys=keys, axis=1, sort=False)
    except TypeError:
        from pandas import Series
        result = Series(results, index=keys, name=self.name)
        if is_nested_object(result):
            raise ValueError('cannot combine transform and aggregation operations')
        return result