@pytest.mark.parametrize('val,exp_dtype', [(1, np.complex128), (1.1, np.complex128), (1 + 1j, np.complex128), (True, np.object)])
def test_setitem_series_complex128(self, val, exp_dtype):
    obj = pd.Series([1 + 1j, 2 + 2j, 3 + 3j, 4 + 4j])
    assert obj.dtype == np.complex128
    exp = pd.Series([1 + 1j, val, 3 + 3j, 4 + 4j])
    self._assert_setitem_series_conversion(obj, val, exp, exp_dtype)