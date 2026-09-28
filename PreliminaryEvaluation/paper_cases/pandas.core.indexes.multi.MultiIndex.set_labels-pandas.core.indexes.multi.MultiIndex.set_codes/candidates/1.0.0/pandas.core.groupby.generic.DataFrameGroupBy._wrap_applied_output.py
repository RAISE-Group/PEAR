def _wrap_applied_output(self, keys, values, not_indexed_same=False):
    if len(keys) == 0:
        return DataFrame(index=keys)
    key_names = self.grouper.names

    def first_not_none(values):
        try:
            return next(com.not_none(*values))
        except StopIteration:
            return None
    v = first_not_none(values)
    if v is None:
        return DataFrame()
    elif isinstance(v, DataFrame):
        return self._concat_objects(keys, values, not_indexed_same=not_indexed_same)
    elif self.grouper.groupings is not None:
        if len(self.grouper.groupings) > 1:
            key_index = self.grouper.result_index
        else:
            ping = self.grouper.groupings[0]
            if len(keys) == ping.ngroups:
                key_index = ping.group_index
                key_index.name = key_names[0]
                key_lookup = Index(keys)
                indexer = key_lookup.get_indexer(key_index)
                values = [values[i] for i in indexer]
            else:
                key_index = Index(keys, name=key_names[0])
            if not self.as_index:
                key_index = None
        v = first_not_none(values)
        if v is None:
            return DataFrame()
        elif isinstance(v, NDFrame):
            kwargs = v._construct_axes_dict()
            if v._constructor is Series:
                backup = create_series_with_explicit_dtype(**kwargs, dtype_if_empty=object)
            else:
                backup = v._constructor(**kwargs)
            values = [x if x is not None else backup for x in values]
        v = values[0]
        if isinstance(v, (np.ndarray, Index, Series)):
            if isinstance(v, Series):
                applied_index = self._selected_obj._get_axis(self.axis)
                all_indexed_same = all_indexes_same([x.index for x in values])
                singular_series = len(values) == 1 and applied_index.nlevels == 1
                if self.squeeze:
                    if singular_series:
                        values[0].name = keys[0]
                        return self._concat_objects(keys, values, not_indexed_same=not_indexed_same)
                    elif all_indexed_same:
                        from pandas.core.reshape.concat import concat
                        return concat(values)
                if not all_indexed_same:
                    return self._concat_objects(keys, values, not_indexed_same=True)
            if self.axis == 0 and isinstance(v, ABCSeries):
                index = v.index.copy()
                if index.name is None:
                    names = {v.name for v in values}
                    if len(names) == 1:
                        index.name = list(names)[0]
                if isinstance(v.index, MultiIndex) or key_index is None or isinstance(key_index, MultiIndex):
                    stacked_values = np.vstack([np.asarray(v) for v in values])
                    result = DataFrame(stacked_values, index=key_index, columns=index)
                else:
                    from pandas.core.reshape.concat import concat
                    result = concat(values, keys=key_index, names=key_index.names, axis=self.axis).unstack()
                    result.columns = index
            elif isinstance(v, ABCSeries):
                stacked_values = np.vstack([np.asarray(v) for v in values])
                result = DataFrame(stacked_values.T, index=v.index, columns=key_index)
            else:
                return Series(values, index=key_index, name=self._selection_name)
            so = self._selected_obj
            if so.ndim == 2 and so.dtypes.apply(needs_i8_conversion).any():
                result = _recast_datetimelike_result(result)
            else:
                result = result._convert(datetime=True)
            return self._reindex_output(result)
        else:
            should_coerce = any((isinstance(x, Timestamp) for x in values))
            return Series(values, index=key_index)._convert(datetime=True, coerce=should_coerce)
    else:
        return self._concat_objects(keys, values, not_indexed_same=not_indexed_same)