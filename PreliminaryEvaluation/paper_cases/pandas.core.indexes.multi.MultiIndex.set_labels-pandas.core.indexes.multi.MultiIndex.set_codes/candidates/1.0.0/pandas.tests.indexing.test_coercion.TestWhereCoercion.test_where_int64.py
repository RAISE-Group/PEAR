@pytest.mark.parametrize('fill_val,exp_dtype', [(1, np.int64), (1.1, np.float64), (1 + 1j, np.complex128), (True, np.object)])
def test_where_int64(self, index_or_series, fill_val, exp_dtype):
    klass = index_or_series
    if klass is pd.Index and exp_dtype is np.complex128:
        pytest.skip('Complex Index not supported')
    obj = klass([1, 2, 3, 4])
    assert obj.dtype == np.int64
    cond = klass([True, False, True, False])
    exp = klass([1, fill_val, 3, fill_val])
    self._assert_where_conversion(obj, cond, fill_val, exp, exp_dtype)
    if fill_val is True:
        values = klass([True, False, True, True])
    else:
        values = klass((x * fill_val for x in [5, 6, 7, 8]))
    exp = klass([1, values[1], 3, values[3]])
    self._assert_where_conversion(obj, cond, values, exp, exp_dtype)