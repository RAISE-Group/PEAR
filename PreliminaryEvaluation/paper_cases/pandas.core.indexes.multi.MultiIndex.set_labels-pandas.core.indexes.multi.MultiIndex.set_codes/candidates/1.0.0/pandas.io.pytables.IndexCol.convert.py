def convert(self, values: np.ndarray, nan_rep, encoding: str, errors: str):
    """
        Convert the data from this selection to the appropriate pandas type.
        """
    assert isinstance(values, np.ndarray), type(values)
    if values.dtype.fields is not None:
        values = values[self.cname]
    val_kind = _ensure_decoded(self.kind)
    values = _maybe_convert(values, val_kind, encoding, errors)
    kwargs = dict()
    kwargs['name'] = _ensure_decoded(self.index_name)
    if self.freq is not None:
        kwargs['freq'] = _ensure_decoded(self.freq)
    try:
        new_pd_index = Index(values, **kwargs)
    except ValueError:
        if 'freq' in kwargs:
            kwargs['freq'] = None
        new_pd_index = Index(values, **kwargs)
    new_pd_index = _set_tz(new_pd_index, self.tz)
    return (new_pd_index, new_pd_index)