def test_cummin_timedelta64(self):
    s = pd.Series(pd.to_timedelta(['NaT', '2 min', 'NaT', '1 min', 'NaT', '3 min']))
    expected = pd.Series(pd.to_timedelta(['NaT', '2 min', 'NaT', '1 min', 'NaT', '1 min']))
    result = s.cummin(skipna=True)
    tm.assert_series_equal(expected, result)
    expected = pd.Series(pd.to_timedelta(['NaT', '2 min', '2 min', '1 min', '1 min', '1 min']))
    result = s.cummin(skipna=False)
    tm.assert_series_equal(expected, result)