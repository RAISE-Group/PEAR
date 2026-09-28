def test_datetime64_tz_dropna(self):
    s = Series([Timestamp('2011-01-01 10:00'), pd.NaT, Timestamp('2011-01-03 10:00'), pd.NaT])
    result = s.dropna()
    expected = Series([Timestamp('2011-01-01 10:00'), Timestamp('2011-01-03 10:00')], index=[0, 2])
    tm.assert_series_equal(result, expected)
    idx = pd.DatetimeIndex(['2011-01-01 10:00', pd.NaT, '2011-01-03 10:00', pd.NaT], tz='Asia/Tokyo')
    s = pd.Series(idx)
    assert s.dtype == 'datetime64[ns, Asia/Tokyo]'
    result = s.dropna()
    expected = Series([Timestamp('2011-01-01 10:00', tz='Asia/Tokyo'), Timestamp('2011-01-03 10:00', tz='Asia/Tokyo')], index=[0, 2])
    assert result.dtype == 'datetime64[ns, Asia/Tokyo]'
    tm.assert_series_equal(result, expected)