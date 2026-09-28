def _getitem_tuple(self, tup: Tuple):
    try:
        return self._getitem_lowerdim(tup)
    except IndexingError:
        pass
    self._has_valid_tuple(tup)
    if self._multi_take_opportunity(tup):
        return self._multi_take(tup)
    retval = self.obj
    for i, key in enumerate(tup):
        if com.is_null_slice(key):
            continue
        retval = getattr(retval, self.name)._getitem_axis(key, axis=i)
    return retval