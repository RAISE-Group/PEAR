@pytest.mark.parametrize('val,exp_dtype', [(1, np.int64), (3, np.int64), (1.1, np.float64), (1 + 1j, np.complex128), (True, np.bool)])
def test_setitem_series_bool(self, val, exp_dtype):
    obj = pd.Series([True, False, True, False])
    assert obj.dtype == np.bool
    if exp_dtype is np.int64:
        exp = pd.Series([True, True, True, False])
        self._assert_setitem_series_conversion(obj, val, exp, np.bool)
        pytest.xfail('TODO_GH12747 The result must be int')
    elif exp_dtype is np.float64:
        exp = pd.Series([True, True, True, False])
        self._assert_setitem_series_conversion(obj, val, exp, np.bool)
        pytest.xfail('TODO_GH12747 The result must be float')
    elif exp_dtype is np.complex128:
        exp = pd.Series([True, True, True, False])
        self._assert_setitem_series_conversion(obj, val, exp, np.bool)
        pytest.xfail('TODO_GH12747 The result must be complex')
    exp = pd.Series([True, val, True, False])
    self._assert_setitem_series_conversion(obj, val, exp, exp_dtype)