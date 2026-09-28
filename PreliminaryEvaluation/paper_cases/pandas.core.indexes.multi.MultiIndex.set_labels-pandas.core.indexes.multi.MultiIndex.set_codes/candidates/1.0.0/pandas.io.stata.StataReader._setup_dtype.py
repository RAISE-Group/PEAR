def _setup_dtype(self):
    """Map between numpy and state dtypes"""
    if self._dtype is not None:
        return self._dtype
    dtype = []
    for i, typ in enumerate(self.typlist):
        if typ in self.NUMPY_TYPE_MAP:
            dtype.append(('s' + str(i), self.byteorder + self.NUMPY_TYPE_MAP[typ]))
        else:
            dtype.append(('s' + str(i), 'S' + str(typ)))
    dtype = np.dtype(dtype)
    self._dtype = dtype
    return self._dtype