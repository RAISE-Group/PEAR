@pytest.mark.parametrize('val,exp_dtype', [(np.int32(1), np.int8), (np.int16(2 ** 9), np.int16)])
def test_setitem_series_int8(self, val, exp_dtype):
    obj = pd.Series([1, 2, 3, 4], dtype=np.int8)
    assert obj.dtype == np.int8
    if exp_dtype is np.int16:
        exp = pd.Series([1, 0, 3, 4], dtype=np.int8)
        self._assert_setitem_series_conversion(obj, val, exp, np.int8)
        pytest.xfail('BUG: it must be Series([1, 1, 3, 4], dtype=np.int16')
    exp = pd.Series([1, val, 3, 4], dtype=np.int8)
    self._assert_setitem_series_conversion(obj, val, exp, exp_dtype)