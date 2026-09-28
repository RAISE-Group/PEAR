def process_axes(self, obj, selection: 'Selection', columns=None):
    """ process axes filters """
    if columns is not None:
        columns = list(columns)
    if columns is not None and self.is_multi_index:
        assert isinstance(self.levels, list)
        for n in self.levels:
            if n not in columns:
                columns.insert(0, n)
    for axis, labels in self.non_index_axes:
        obj = _reindex_axis(obj, axis, labels, columns)
    if selection.filter is not None:
        for field, op, filt in selection.filter.format():

            def process_filter(field, filt):
                for axis_name in obj._AXIS_NAMES.values():
                    axis_number = obj._get_axis_number(axis_name)
                    axis_values = obj._get_axis(axis_name)
                    assert axis_number is not None
                    if field == axis_name:
                        if self.is_multi_index:
                            filt = filt.union(Index(self.levels))
                        takers = op(axis_values, filt)
                        return obj.loc(axis=axis_number)[takers]
                    elif field in axis_values:
                        values = ensure_index(getattr(obj, field).values)
                        filt = ensure_index(filt)
                        if isinstance(obj, DataFrame):
                            axis_number = 1 - axis_number
                        takers = op(values, filt)
                        return obj.loc(axis=axis_number)[takers]
                raise ValueError(f'cannot find the field [{field}] for filtering!')
            obj = process_filter(field, filt)
    return obj