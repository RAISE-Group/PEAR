def test_resample_ambiguous_time_bin_edge(self):
    idx = pd.date_range('2014-10-25 22:00:00', '2014-10-26 00:30:00', freq='30T', tz='Europe/London')
    expected = Series(np.zeros(len(idx)), index=idx)
    result = expected.resample('30T').mean()
    tm.assert_series_equal(result, expected)