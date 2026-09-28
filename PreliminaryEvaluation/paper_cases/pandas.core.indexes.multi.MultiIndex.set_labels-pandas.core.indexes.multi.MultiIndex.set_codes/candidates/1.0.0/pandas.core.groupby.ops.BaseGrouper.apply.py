def apply(self, f, data: FrameOrSeries, axis: int=0):
    mutated = self.mutated
    splitter = self._get_splitter(data, axis=axis)
    group_keys = self._get_group_keys()
    result_values = None
    sdata: FrameOrSeries = splitter._get_sorted_data()
    if sdata.ndim == 2 and np.any(sdata.dtypes.apply(is_extension_array_dtype)):
        pass
    elif com.get_callable_name(f) not in base.plotting_methods and isinstance(splitter, FrameSplitter) and (axis == 0) and (not sdata.index._has_complex_internals):
        try:
            result_values, mutated = splitter.fast_apply(f, group_keys)
        except libreduction.InvalidApply as err:
            if 'Let this error raise above us' not in str(err):
                raise
        else:
            if len(result_values) == len(group_keys):
                return (group_keys, result_values, mutated)
    for key, (i, group) in zip(group_keys, splitter):
        object.__setattr__(group, 'name', key)
        if result_values is None:
            result_values = []
        elif i == 0:
            continue
        group_axes = group.axes
        res = f(group)
        if not _is_indexed_like(res, group_axes):
            mutated = True
        result_values.append(res)
    return (group_keys, result_values, mutated)