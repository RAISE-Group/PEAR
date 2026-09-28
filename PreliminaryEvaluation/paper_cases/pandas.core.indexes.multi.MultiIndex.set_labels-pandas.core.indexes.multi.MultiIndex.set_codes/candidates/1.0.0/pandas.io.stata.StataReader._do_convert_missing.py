def _do_convert_missing(self, data, convert_missing):
    replacements = {}
    for i, colname in enumerate(data):
        fmt = self.typlist[i]
        if fmt not in self.VALID_RANGE:
            continue
        nmin, nmax = self.VALID_RANGE[fmt]
        series = data[colname]
        missing = np.logical_or(series < nmin, series > nmax)
        if not missing.any():
            continue
        if convert_missing:
            missing_loc = np.argwhere(missing._ndarray_values)
            umissing, umissing_loc = np.unique(series[missing], return_inverse=True)
            replacement = Series(series, dtype=np.object)
            for j, um in enumerate(umissing):
                missing_value = StataMissingValue(um)
                loc = missing_loc[umissing_loc == j]
                replacement.iloc[loc] = missing_value
        else:
            dtype = series.dtype
            if dtype not in (np.float32, np.float64):
                dtype = np.float64
            replacement = Series(series, dtype=dtype)
            replacement[missing] = np.nan
        replacements[colname] = replacement
    if replacements:
        columns = data.columns
        replacements = DataFrame(replacements)
        data = concat([data.drop(replacements.columns, 1), replacements], 1)
        data = data[columns]
    return data