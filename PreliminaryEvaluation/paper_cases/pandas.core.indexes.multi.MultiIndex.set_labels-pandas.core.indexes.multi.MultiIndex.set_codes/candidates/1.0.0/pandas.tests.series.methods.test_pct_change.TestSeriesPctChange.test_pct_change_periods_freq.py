@pytest.mark.parametrize('freq, periods, fill_method, limit', [('5B', 5, None, None), ('3B', 3, None, None), ('3B', 3, 'bfill', None), ('7B', 7, 'pad', 1), ('7B', 7, 'bfill', 3), ('14B', 14, None, None)])
def test_pct_change_periods_freq(self, freq, periods, fill_method, limit, datetime_series):
    rs_freq = datetime_series.pct_change(freq=freq, fill_method=fill_method, limit=limit)
    rs_periods = datetime_series.pct_change(periods, fill_method=fill_method, limit=limit)
    tm.assert_series_equal(rs_freq, rs_periods)
    empty_ts = Series(index=datetime_series.index, dtype=object)
    rs_freq = empty_ts.pct_change(freq=freq, fill_method=fill_method, limit=limit)
    rs_periods = empty_ts.pct_change(periods, fill_method=fill_method, limit=limit)
    tm.assert_series_equal(rs_freq, rs_periods)