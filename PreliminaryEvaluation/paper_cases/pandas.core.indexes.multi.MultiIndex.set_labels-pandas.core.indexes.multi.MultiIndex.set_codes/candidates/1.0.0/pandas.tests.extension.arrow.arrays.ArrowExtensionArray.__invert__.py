def __invert__(self):
    return type(self).from_scalars(~self._data.to_pandas())