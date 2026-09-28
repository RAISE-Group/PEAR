def test_asfreq(self):
    ts = Series([0.0, 1.0, 2.0], index=[datetime(2009, 10, 30), datetime(2009, 11, 30), datetime(2009, 12, 31)])
    daily_ts = ts.asfreq('B')
    monthly_ts = daily_ts.asfreq('BM')
    tm.assert_series_equal(monthly_ts, ts)
    daily_ts = ts.asfreq('B', method='pad')
    monthly_ts = daily_ts.asfreq('BM')
    tm.assert_series_equal(monthly_ts, ts)
    daily_ts = ts.asfreq(BDay())
    monthly_ts = daily_ts.asfreq(BMonthEnd())
    tm.assert_series_equal(monthly_ts, ts)
    result = ts[:0].asfreq('M')
    assert len(result) == 0
    assert result is not ts
    daily_ts = ts.asfreq('D', fill_value=-1)
    result = daily_ts.value_counts().sort_index()
    expected = Series([60, 1, 1, 1], index=[-1.0, 2.0, 1.0, 0.0]).sort_index()
    tm.assert_series_equal(result, expected)