@staticmethod
def _get_call_args(backend_name, data, args, kwargs):
    """
        This function makes calls to this accessor `__call__` method compatible
        with the previous `SeriesPlotMethods.__call__` and
        `DataFramePlotMethods.__call__`. Those had slightly different
        signatures, since `DataFramePlotMethods` accepted `x` and `y`
        parameters.
        """
    if isinstance(data, ABCSeries):
        arg_def = [('kind', 'line'), ('ax', None), ('figsize', None), ('use_index', True), ('title', None), ('grid', None), ('legend', False), ('style', None), ('logx', False), ('logy', False), ('loglog', False), ('xticks', None), ('yticks', None), ('xlim', None), ('ylim', None), ('rot', None), ('fontsize', None), ('colormap', None), ('table', False), ('yerr', None), ('xerr', None), ('label', None), ('secondary_y', False)]
    elif isinstance(data, ABCDataFrame):
        arg_def = [('x', None), ('y', None), ('kind', 'line'), ('ax', None), ('subplots', False), ('sharex', None), ('sharey', False), ('layout', None), ('figsize', None), ('use_index', True), ('title', None), ('grid', None), ('legend', True), ('style', None), ('logx', False), ('logy', False), ('loglog', False), ('xticks', None), ('yticks', None), ('xlim', None), ('ylim', None), ('rot', None), ('fontsize', None), ('colormap', None), ('table', False), ('yerr', None), ('xerr', None), ('secondary_y', False), ('sort_columns', False)]
    else:
        raise TypeError(f'Called plot accessor for type {type(data).__name__}, expected Series or DataFrame')
    if args and isinstance(data, ABCSeries):
        positional_args = str(args)[1:-1]
        keyword_args = ', '.join((f'{name}={repr(value)}' for (name, default), value in zip(arg_def, args)))
        msg = f'`Series.plot()` should not be called with positional arguments, only keyword arguments. The order of positional arguments will change in the future. Use `Series.plot({keyword_args})` instead of `Series.plot({positional_args})`.'
        raise TypeError(msg)
    pos_args = {name: value for value, (name, _) in zip(args, arg_def)}
    if backend_name == 'pandas.plotting._matplotlib':
        kwargs = dict(arg_def, **pos_args, **kwargs)
    else:
        kwargs = dict(pos_args, **kwargs)
    x = kwargs.pop('x', None)
    y = kwargs.pop('y', None)
    kind = kwargs.pop('kind', 'line')
    return (x, y, kind, kwargs)