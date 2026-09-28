def test_datetime64_dtype_array_returned(self):
    expected = np_array_datetime64_compat(['2015-01-03T00:00:00.000000000+0000', '2015-01-01T00:00:00.000000000+0000'], dtype='M8[ns]')
    dt_index = pd.to_datetime(['2015-01-03T00:00:00.000000000', '2015-01-01T00:00:00.000000000', '2015-01-01T00:00:00.000000000'])
    result = algos.unique(dt_index)
    tm.assert_numpy_array_equal(result, expected)
    assert result.dtype == expected.dtype
    s = Series(dt_index)
    result = algos.unique(s)
    tm.assert_numpy_array_equal(result, expected)
    assert result.dtype == expected.dtype
    arr = s.values
    result = algos.unique(arr)
    tm.assert_numpy_array_equal(result, expected)
    assert result.dtype == expected.dtype