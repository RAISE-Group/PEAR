@Appender(Index.astype.__doc__)
def astype(self, dtype, copy=True):
    if is_dtype_equal(self.dtype, dtype) and copy is False:
        return self
    new_values = self._data.astype(dtype, copy=copy)
    return Index(new_values, dtype=new_values.dtype, name=self.name, copy=False)