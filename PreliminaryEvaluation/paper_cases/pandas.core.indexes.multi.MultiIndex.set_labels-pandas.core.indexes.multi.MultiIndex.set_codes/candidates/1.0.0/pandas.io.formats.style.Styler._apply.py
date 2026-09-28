def _apply(self, func, axis=0, subset=None, **kwargs):
    subset = slice(None) if subset is None else subset
    subset = _non_reducing_slice(subset)
    data = self.data.loc[subset]
    if axis is not None:
        result = data.apply(func, axis=axis, result_type='expand', **kwargs)
        result.columns = data.columns
    else:
        result = func(data, **kwargs)
        if not isinstance(result, pd.DataFrame):
            raise TypeError(f'Function {repr(func)} must return a DataFrame when passed to `Styler.apply` with axis=None')
        if not (result.index.equals(data.index) and result.columns.equals(data.columns)):
            raise ValueError(f'Result of {repr(func)} must have identical index and columns as the input')
    result_shape = result.shape
    expected_shape = self.data.loc[subset].shape
    if result_shape != expected_shape:
        raise ValueError(f'Function {repr(func)} returned the wrong shape.\nResult has shape: {result.shape}\nExpected shape:   {expected_shape}')
    self._update_ctx(result)
    return self