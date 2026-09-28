@pytest.mark.parametrize('fill_val, fill_dtype', [(1, np.object), (1.1, np.object), (1 + 1j, np.object), (True, np.object)])
def test_fillna_object(self, index_or_series, fill_val, fill_dtype):
    klass = index_or_series
    obj = klass(['a', np.nan, 'c', 'd'])
    assert obj.dtype == np.object
    exp = klass(['a', fill_val, 'c', 'd'])
    self._assert_fillna_conversion(obj, fill_val, exp, fill_dtype)