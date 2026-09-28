def _shallow_copy(self, values=None, **kwargs):
    if values is None:
        values = self._data
    if isinstance(values, type(self)):
        values = values._data
    if not isinstance(values, PeriodArray):
        if isinstance(values, np.ndarray) and values.dtype == 'i8':
            values = PeriodArray(values, freq=self.freq)
        else:
            raise TypeError(type(values), getattr(values, 'dtype', None))
    validate_dtype_freq(self.dtype, kwargs.get('freq'))
    attributes = self._get_attributes_dict()
    attributes.update(kwargs)
    if not len(values) and 'dtype' not in kwargs:
        attributes['dtype'] = self.dtype
    return self._simple_new(values, **attributes)