def test_concat_tz_series_tzlocal(self):
    x = [pd.Timestamp('2011-01-01', tz=dateutil.tz.tzlocal()), pd.Timestamp('2011-02-01', tz=dateutil.tz.tzlocal())]
    y = [pd.Timestamp('2012-01-01', tz=dateutil.tz.tzlocal()), pd.Timestamp('2012-02-01', tz=dateutil.tz.tzlocal())]
    result = concat([pd.Series(x), pd.Series(y)], ignore_index=True)
    tm.assert_series_equal(result, pd.Series(x + y))
    assert result.dtype == 'datetime64[ns, tzlocal()]'