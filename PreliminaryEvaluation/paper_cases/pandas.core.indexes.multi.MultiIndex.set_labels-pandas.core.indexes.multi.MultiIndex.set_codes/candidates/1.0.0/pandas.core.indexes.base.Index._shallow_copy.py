@Appender(_index_shared_docs['_shallow_copy'])
def _shallow_copy(self, values=None, **kwargs):
    if values is None:
        values = self.values
    attributes = self._get_attributes_dict()
    attributes.update(kwargs)
    if not len(values) and 'dtype' not in kwargs:
        attributes['dtype'] = self.dtype
    values = getattr(values, '_values', values)
    if isinstance(values, ABCDatetimeArray):
        values = values.asi8
    return self._simple_new(values, **attributes)