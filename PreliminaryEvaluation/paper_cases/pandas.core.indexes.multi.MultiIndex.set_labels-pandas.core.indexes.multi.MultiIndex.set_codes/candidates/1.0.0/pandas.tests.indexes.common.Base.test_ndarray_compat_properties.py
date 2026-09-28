def test_ndarray_compat_properties(self):
    idx = self.create_index()
    assert idx.T.equals(idx)
    assert idx.transpose().equals(idx)
    values = idx.values
    for prop in self._compat_props:
        assert getattr(idx, prop) == getattr(values, prop)
    idx.nbytes
    idx.values.nbytes