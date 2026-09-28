def _aggregate_multiple_funcs(self, arg):
    if isinstance(arg, dict):
        if isinstance(self._selected_obj, Series):
            raise SpecificationError('nested renamer is not supported')
        columns = list(arg.keys())
        arg = arg.items()
    elif any((isinstance(x, (tuple, list)) for x in arg)):
        arg = [(x, x) if not isinstance(x, (tuple, list)) else x for x in arg]
        columns = next(zip(*arg))
    else:
        columns = []
        for f in arg:
            columns.append(com.get_callable_name(f) or f)
        arg = zip(columns, arg)
    results = {}
    for name, func in arg:
        obj = self
        if name in self._selected_obj:
            obj = copy.copy(obj)
            obj._reset_cache()
            obj._selection = name
        results[name] = obj.aggregate(func)
    if any((isinstance(x, DataFrame) for x in results.values())):
        return results
    return DataFrame(results, columns=columns)