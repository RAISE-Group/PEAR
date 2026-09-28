@pytest.mark.parametrize('val,exp_dtype', [(1, np.float64), (1.1, np.float64), (1 + 1j, np.complex128), (True, np.object)])
def test_setitem_series_float64(self, val, exp_dtype):
    obj = pd.Series([1.1, 2.2, 3.3, 4.4])
    assert obj.dtype == np.float64
    exp = pd.Series([1.1, val, 3.3, 4.4])
    self._assert_setitem_series_conversion(obj, val, exp, exp_dtype)