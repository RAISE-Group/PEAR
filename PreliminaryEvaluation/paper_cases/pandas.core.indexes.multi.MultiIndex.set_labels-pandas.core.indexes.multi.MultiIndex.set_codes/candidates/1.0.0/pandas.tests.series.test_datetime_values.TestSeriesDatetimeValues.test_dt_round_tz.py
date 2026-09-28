def test_dt_round_tz(self):
    s = Series(pd.to_datetime(['2012-01-01 13:00:00', '2012-01-01 12:01:00', '2012-01-01 08:00:00']), name='xxx')
    result = s.dt.tz_localize('UTC').dt.tz_convert('US/Eastern').dt.round('D')
    exp_values = pd.to_datetime(['2012-01-01', '2012-01-01', '2012-01-01']).tz_localize('US/Eastern')
    expected = Series(exp_values, name='xxx')
    tm.assert_series_equal(result, expected)