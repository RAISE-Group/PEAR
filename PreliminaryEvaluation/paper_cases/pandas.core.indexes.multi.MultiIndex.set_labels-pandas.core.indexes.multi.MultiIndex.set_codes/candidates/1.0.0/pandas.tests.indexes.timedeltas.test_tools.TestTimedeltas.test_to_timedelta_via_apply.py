def test_to_timedelta_via_apply(self):
    expected = Series([np.timedelta64(1, 's')])
    result = Series(['00:00:01']).apply(to_timedelta)
    tm.assert_series_equal(result, expected)
    result = Series([to_timedelta('00:00:01')])
    tm.assert_series_equal(result, expected)