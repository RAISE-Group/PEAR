@pytest.mark.parametrize('val,exp_dtype', [(1, np.int64), (1.1, np.float64), (1 + 1j, np.complex128), (True, np.object)])
def test_setitem_series_int64(self, val, exp_dtype):
    obj = pd.Series([1, 2, 3, 4])
    assert obj.dtype == np.int64
    if exp_dtype is np.float64:
        exp = pd.Series([1, 1, 3, 4])
        self._assert_setitem_series_conversion(obj, 1.1, exp, np.int64)
        pytest.xfail('GH12747 The result must be float')
    exp = pd.Series([1, val, 3, 4])
    self._assert_setitem_series_conversion(obj, val, exp, exp_dtype)