def test_dti_shift_across_dst(self):
    idx = date_range('2013-11-03', tz='America/Chicago', periods=7, freq='H')
    s = Series(index=idx[:-1], dtype=object)
    result = s.shift(freq='H')
    expected = Series(index=idx[1:], dtype=object)
    tm.assert_series_equal(result, expected)