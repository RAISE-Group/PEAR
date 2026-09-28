@pytest.mark.parametrize('fill_val,exp_dtype', [(1, np.object), (1.1, np.object), (1 + 1j, np.object), (True, np.bool)])
def test_where_series_bool(self, fill_val, exp_dtype):
    obj = pd.Series([True, False, True, False])
    assert obj.dtype == np.bool
    cond = pd.Series([True, False, True, False])
    exp = pd.Series([True, fill_val, True, fill_val])
    self._assert_where_conversion(obj, cond, fill_val, exp, exp_dtype)
    if fill_val is True:
        values = pd.Series([True, False, True, True])
    else:
        values = pd.Series((x * fill_val for x in [5, 6, 7, 8]))
    exp = pd.Series([True, values[1], True, values[3]])
    self._assert_where_conversion(obj, cond, values, exp, exp_dtype)