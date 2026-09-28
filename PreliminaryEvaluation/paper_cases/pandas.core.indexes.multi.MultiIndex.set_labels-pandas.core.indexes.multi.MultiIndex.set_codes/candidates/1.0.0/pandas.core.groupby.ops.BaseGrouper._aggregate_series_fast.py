def _aggregate_series_fast(self, obj: Series, func):
    func = self._is_builtin_func(func)
    group_index, _, ngroups = self.group_info
    dummy = obj._get_values(slice(None, 0))
    indexer = get_group_index_sorter(group_index, ngroups)
    obj = obj.take(indexer)
    group_index = algorithms.take_nd(group_index, indexer, allow_fill=False)
    grouper = libreduction.SeriesGrouper(obj, func, group_index, ngroups, dummy)
    result, counts = grouper.get_result()
    return (result, counts)