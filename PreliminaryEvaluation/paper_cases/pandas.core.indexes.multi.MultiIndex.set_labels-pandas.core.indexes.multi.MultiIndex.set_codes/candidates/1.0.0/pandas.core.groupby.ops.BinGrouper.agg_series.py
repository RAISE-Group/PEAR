def agg_series(self, obj: Series, func):
    assert self.ngroups != 0
    assert len(self.bins) > 0
    if is_extension_array_dtype(obj.dtype):
        return self._aggregate_series_pure_python(obj, func)
    dummy = obj[:0]
    grouper = libreduction.SeriesBinGrouper(obj, func, self.bins, dummy)
    return grouper.get_result()