@pytest.mark.parametrize('fill_val,exp_dtype', [(1, np.complex128), (1.1, np.complex128), (1 + 1j, np.complex128), (True, np.object)])
def test_where_series_complex128(self, fill_val, exp_dtype):
    obj = pd.Series([1 + 1j, 2 + 2j, 3 + 3j, 4 + 4j])
    assert obj.dtype == np.complex128
    cond = pd.Series([True, False, True, False])
    exp = pd.Series([1 + 1j, fill_val, 3 + 3j, fill_val])
    self._assert_where_conversion(obj, cond, fill_val, exp, exp_dtype)
    if fill_val is True:
        values = pd.Series([True, False, True, True])
    else:
        values = pd.Series((x * fill_val for x in [5, 6, 7, 8]))
    exp = pd.Series([1 + 1j, values[1], 3 + 3j, values[3]])
    self._assert_where_conversion(obj, cond, values, exp, exp_dtype)