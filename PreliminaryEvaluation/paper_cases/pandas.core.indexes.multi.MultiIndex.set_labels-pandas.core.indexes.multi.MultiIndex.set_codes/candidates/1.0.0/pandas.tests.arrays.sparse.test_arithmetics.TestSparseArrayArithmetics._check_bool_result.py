def _check_bool_result(self, res):
    assert isinstance(res, self._klass)
    assert isinstance(res.dtype, SparseDtype)
    assert res.dtype.subtype == np.bool
    assert isinstance(res.fill_value, bool)