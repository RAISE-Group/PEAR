def quantile(self, qs, interpolation='linear', axis=0):
    """
        compute the quantiles of the

        Parameters
        ----------
        qs: a scalar or list of the quantiles to be computed
        interpolation: type of interpolation, default 'linear'
        axis: axis to compute, default 0

        Returns
        -------
        Block
        """
    assert self.ndim == 2
    values = self.get_values()
    is_empty = values.shape[axis] == 0
    orig_scalar = not is_list_like(qs)
    if orig_scalar:
        qs = [qs]
    if is_empty:
        result = np.repeat(np.array([self.fill_value] * len(qs)), len(values)).reshape(len(values), len(qs))
    else:
        mask = np.asarray(isna(values))
        result = nanpercentile(values, np.array(qs) * 100, axis=axis, na_value=self.fill_value, mask=mask, ndim=values.ndim, interpolation=interpolation)
        result = np.array(result, copy=False)
        result = result.T
    if orig_scalar and (not lib.is_scalar(result)):
        assert result.shape[-1] == 1, result.shape
        result = result[..., 0]
        result = lib.item_from_zerodim(result)
    ndim = np.ndim(result)
    return make_block(result, placement=np.arange(len(result)), ndim=ndim)