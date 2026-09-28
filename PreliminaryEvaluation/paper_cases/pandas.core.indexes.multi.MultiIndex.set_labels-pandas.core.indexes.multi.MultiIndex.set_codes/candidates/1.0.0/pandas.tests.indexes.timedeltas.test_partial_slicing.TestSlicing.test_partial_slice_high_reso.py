def test_partial_slice_high_reso(self):
    rng = timedelta_range('1 day 10:11:12', freq='us', periods=2000)
    s = Series(np.arange(len(rng)), index=rng)
    result = s['1 day 10:11:12':]
    expected = s.iloc[0:]
    tm.assert_series_equal(result, expected)
    result = s['1 day 10:11:12.001':]
    expected = s.iloc[1000:]
    tm.assert_series_equal(result, expected)
    result = s['1 days, 10:11:12.001001']
    assert result == s.iloc[1001]