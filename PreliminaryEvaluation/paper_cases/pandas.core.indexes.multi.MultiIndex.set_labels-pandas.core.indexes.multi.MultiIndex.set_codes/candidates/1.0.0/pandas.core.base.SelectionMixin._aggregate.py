def _aggregate(self, arg, *args, **kwargs):
    """
        provide an implementation for the aggregators

        Parameters
        ----------
        arg : string, dict, function
        *args : args to pass on to the function
        **kwargs : kwargs to pass on to the function

        Returns
        -------
        tuple of result, how

        Notes
        -----
        how can be a string describe the required post-processing, or
        None if not required
        """
    is_aggregator = lambda x: isinstance(x, (list, tuple, dict))
    _axis = kwargs.pop('_axis', None)
    if _axis is None:
        _axis = getattr(self, 'axis', 0)
    if isinstance(arg, str):
        return (self._try_aggregate_string_function(arg, *args, **kwargs), None)
    if isinstance(arg, dict):
        if _axis != 0:
            raise ValueError('Can only pass dict with axis=0')
        obj = self._selected_obj
        if any((is_aggregator(x) for x in arg.values())):
            new_arg = {}
            for k, v in arg.items():
                if not isinstance(v, (tuple, list, dict)):
                    new_arg[k] = [v]
                else:
                    new_arg[k] = v
                if isinstance(v, dict):
                    raise SpecificationError('nested renamer is not supported')
                elif isinstance(obj, ABCSeries):
                    raise SpecificationError('nested renamer is not supported')
                elif isinstance(obj, ABCDataFrame) and k not in obj.columns:
                    raise KeyError(f"Column '{k}' does not exist!")
            arg = new_arg
        else:
            keys = list(arg.keys())
            if isinstance(obj, ABCDataFrame) and len(obj.columns.intersection(keys)) != len(keys):
                raise SpecificationError('nested renamer is not supported')
        from pandas.core.reshape.concat import concat

        def _agg_1dim(name, how, subset=None):
            """
                aggregate a 1-dim with how
                """
            colg = self._gotitem(name, ndim=1, subset=subset)
            if colg.ndim != 1:
                raise SpecificationError('nested dictionary is ambiguous in aggregation')
            return colg.aggregate(how)

        def _agg_2dim(name, how):
            """
                aggregate a 2-dim with how
                """
            colg = self._gotitem(self._selection, ndim=2, subset=obj)
            return colg.aggregate(how)

        def _agg(arg, func):
            """
                run the aggregations over the arg with func
                return a dict
                """
            result = {}
            for fname, agg_how in arg.items():
                result[fname] = func(fname, agg_how)
            return result
        keys = list(arg.keys())
        result = {}
        if self._selection is not None:
            sl = set(self._selection_list)
            if len(sl) == 1:
                result = _agg(arg, lambda fname, agg_how: _agg_1dim(self._selection, agg_how))
            elif not len(sl - set(keys)):
                result = _agg(arg, _agg_1dim)
            else:
                result = _agg(arg, _agg_2dim)
        else:
            try:
                result = _agg(arg, _agg_1dim)
            except SpecificationError:
                result = _agg(arg, _agg_2dim)

        def is_any_series() -> bool:
            return any((isinstance(r, ABCSeries) for r in result.values()))

        def is_any_frame() -> bool:
            return any((isinstance(r, ABCDataFrame) for r in result.values()))
        if isinstance(result, list):
            return (concat(result, keys=keys, axis=1, sort=True), True)
        elif is_any_frame():
            return (concat([result[k] for k in keys], keys=keys, axis=1), True)
        elif isinstance(self, ABCSeries) and is_any_series():
            try:
                result = concat(result)
            except TypeError:
                raise ValueError('cannot perform both aggregation and transformation operations simultaneously')
            return (result, True)
        from pandas import DataFrame, Series
        try:
            result = DataFrame(result)
        except ValueError:
            result = Series(result, name=getattr(self, 'name', None))
        return (result, True)
    elif is_list_like(arg):
        return (self._aggregate_multiple_funcs(arg, _axis=_axis), None)
    else:
        result = None
    f = self._get_cython_func(arg)
    if f and (not args) and (not kwargs):
        return (getattr(self, f)(), None)
    return (result, True)