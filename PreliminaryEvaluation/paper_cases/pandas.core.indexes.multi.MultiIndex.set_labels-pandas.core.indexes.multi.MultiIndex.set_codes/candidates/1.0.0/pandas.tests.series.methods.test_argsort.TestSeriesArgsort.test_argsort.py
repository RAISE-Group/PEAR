def test_argsort(self, datetime_series):
    self._check_accum_op('argsort', datetime_series, check_dtype=False)
    argsorted = datetime_series.argsort()
    assert issubclass(argsorted.dtype.type, np.integer)
    s = Series([Timestamp('201301{i:02d}'.format(i=i)) for i in range(1, 6)])
    assert s.dtype == 'datetime64[ns]'
    shifted = s.shift(-1)
    assert shifted.dtype == 'datetime64[ns]'
    assert isna(shifted[4])
    result = s.argsort()
    expected = Series(range(5), dtype='int64')
    tm.assert_series_equal(result, expected)
    result = shifted.argsort()
    expected = Series(list(range(4)) + [-1], dtype='int64')
    tm.assert_series_equal(result, expected)