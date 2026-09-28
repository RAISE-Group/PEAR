def test_astype_timedelta64(self):
    idx = TimedeltaIndex([100000000000000.0, 'NaT', NaT, np.NaN])
    result = idx.astype('timedelta64')
    expected = Float64Index([100000000000000.0] + [np.NaN] * 3, dtype='float64')
    tm.assert_index_equal(result, expected)
    result = idx.astype('timedelta64[ns]')
    tm.assert_index_equal(result, idx)
    assert result is not idx
    result = idx.astype('timedelta64[ns]', copy=False)
    tm.assert_index_equal(result, idx)
    assert result is idx