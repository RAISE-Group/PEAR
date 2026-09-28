@pytest.mark.parametrize('tz', [None, 'US/Pacific'])
def test_cummin_datetime64(self, tz):
    s = pd.Series(pd.to_datetime(['NaT', '2000-1-2', 'NaT', '2000-1-1', 'NaT', '2000-1-3']).tz_localize(tz))
    expected = pd.Series(pd.to_datetime(['NaT', '2000-1-2', 'NaT', '2000-1-1', 'NaT', '2000-1-1']).tz_localize(tz))
    result = s.cummin(skipna=True)
    tm.assert_series_equal(expected, result)
    expected = pd.Series(pd.to_datetime(['NaT', '2000-1-2', '2000-1-2', '2000-1-1', '2000-1-1', '2000-1-1']).tz_localize(tz))
    result = s.cummin(skipna=False)
    tm.assert_series_equal(expected, result)