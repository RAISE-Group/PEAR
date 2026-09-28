def __getitem__(self, key):
    if type(key) is tuple:
        key = tuple((com.apply_if_callable(x, self.obj) for x in key))
        try:
            values = self.obj._get_value(*key)
        except (KeyError, TypeError, InvalidIndexError, AttributeError):
            pass
        else:
            if is_scalar(values):
                return values
        return self._getitem_tuple(key)
    else:
        axis = self.axis or 0
        key = com.apply_if_callable(key, self.obj)
        return self._getitem_axis(key, axis=axis)