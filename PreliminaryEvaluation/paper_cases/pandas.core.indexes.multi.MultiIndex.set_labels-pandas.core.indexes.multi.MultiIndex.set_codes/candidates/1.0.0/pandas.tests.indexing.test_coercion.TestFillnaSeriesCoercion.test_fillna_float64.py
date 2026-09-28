@pytest.mark.parametrize('fill_val,fill_dtype', [(1, np.float64), (1.1, np.float64), (1 + 1j, np.complex128), (True, np.object)])
def test_fillna_float64(self, index_or_series, fill_val, fill_dtype):
    klass = index_or_series
    obj = klass([1.1, np.nan, 3.3, 4.4])
    assert obj.dtype == np.float64
    exp = klass([1.1, fill_val, 3.3, 4.4])
    if fill_dtype == np.complex128 and klass == pd.Index:
        fill_dtype = np.object
    self._assert_fillna_conversion(obj, fill_val, exp, fill_dtype)