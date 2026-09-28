def _delegate_property_get(self, name):
    from pandas import Series
    values = self._get_values()
    result = getattr(values, name)
    if isinstance(result, np.ndarray):
        if is_integer_dtype(result):
            result = result.astype('int64')
    elif not is_list_like(result):
        return result
    result = np.asarray(result)
    if self.orig is not None:
        index = self.orig.index
    else:
        index = self._parent.index
    result = Series(result, index=index, name=self.name)
    result._is_copy = 'modifications to a property of a datetimelike object are not supported and are discarded. Change values on the original.'
    return result