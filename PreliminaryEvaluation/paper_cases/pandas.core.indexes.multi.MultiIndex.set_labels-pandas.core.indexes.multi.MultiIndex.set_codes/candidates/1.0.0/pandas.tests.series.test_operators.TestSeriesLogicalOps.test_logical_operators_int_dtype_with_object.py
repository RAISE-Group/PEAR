def test_logical_operators_int_dtype_with_object(self):
    s_0123 = Series(range(4), dtype='int64')
    result = s_0123 & Series([False, np.NaN, False, False])
    expected = Series([False] * 4)
    tm.assert_series_equal(result, expected)
    s_abNd = Series(['a', 'b', np.NaN, 'd'])
    with pytest.raises(TypeError, match="unsupported.* 'int' and 'str'"):
        s_0123 & s_abNd