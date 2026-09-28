@pytest.mark.parametrize('fill_val,exp_dtype', [(1, np.object), (1.1, np.object), (1 + 1j, np.object), (True, np.object)])
def test_where_object(self, index_or_series, fill_val, exp_dtype):
    klass = index_or_series
    obj = klass(list('abcd'))
    assert obj.dtype == np.object
    cond = klass([True, False, True, False])
    if fill_val is True and klass is pd.Series:
        ret_val = 1
    else:
        ret_val = fill_val
    exp = klass(['a', ret_val, 'c', ret_val])
    self._assert_where_conversion(obj, cond, fill_val, exp, exp_dtype)
    if fill_val is True:
        values = klass([True, False, True, True])
    else:
        values = klass((fill_val * x for x in [5, 6, 7, 8]))
    exp = klass(['a', values[1], 'c', values[3]])
    self._assert_where_conversion(obj, cond, values, exp, exp_dtype)