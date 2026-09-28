def test_truncate(self, datetime_series):
    offset = BDay()
    ts = datetime_series[::3]
    start, end = (datetime_series.index[3], datetime_series.index[6])
    start_missing, end_missing = (datetime_series.index[2], datetime_series.index[7])
    truncated = ts.truncate()
    tm.assert_series_equal(truncated, ts)
    expected = ts[1:3]
    truncated = ts.truncate(start, end)
    tm.assert_series_equal(truncated, expected)
    truncated = ts.truncate(start_missing, end_missing)
    tm.assert_series_equal(truncated, expected)
    expected = ts[1:]
    truncated = ts.truncate(before=start)
    tm.assert_series_equal(truncated, expected)
    truncated = ts.truncate(before=start_missing)
    tm.assert_series_equal(truncated, expected)
    expected = ts[:3]
    truncated = ts.truncate(after=end)
    tm.assert_series_equal(truncated, expected)
    truncated = ts.truncate(after=end_missing)
    tm.assert_series_equal(truncated, expected)
    truncated = ts.truncate(after=datetime_series.index[0] - offset)
    assert len(truncated) == 0
    truncated = ts.truncate(before=datetime_series.index[-1] + offset)
    assert len(truncated) == 0
    msg = 'Truncate: 1999-12-31 00:00:00 must be after 2000-02-14 00:00:00'
    with pytest.raises(ValueError, match=msg):
        ts.truncate(before=datetime_series.index[-1] + offset, after=datetime_series.index[0] - offset)