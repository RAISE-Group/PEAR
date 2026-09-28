def test_cmp_dt64_arraylike_tznaive(self, all_compare_operators):
    opname = all_compare_operators.strip('_')
    op = getattr(operator, opname)
    dti = pd.date_range('2016-01-1', freq='MS', periods=9, tz=None)
    arr = DatetimeArray(dti)
    assert arr.freq == dti.freq
    assert arr.tz == dti.tz
    right = dti
    expected = np.ones(len(arr), dtype=bool)
    if opname in ['ne', 'gt', 'lt']:
        expected = ~expected
    result = op(arr, arr)
    tm.assert_numpy_array_equal(result, expected)
    for other in [right, np.array(right)]:
        result = op(arr, other)
        tm.assert_numpy_array_equal(result, expected)
        result = op(other, arr)
        tm.assert_numpy_array_equal(result, expected)