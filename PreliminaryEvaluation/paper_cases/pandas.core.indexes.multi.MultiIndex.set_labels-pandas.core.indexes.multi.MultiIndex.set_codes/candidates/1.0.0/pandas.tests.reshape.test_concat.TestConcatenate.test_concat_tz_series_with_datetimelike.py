def test_concat_tz_series_with_datetimelike(self):
    x = [pd.Timestamp('2011-01-01', tz='US/Eastern'), pd.Timestamp('2011-02-01', tz='US/Eastern')]
    y = [pd.Timedelta('1 day'), pd.Timedelta('2 day')]
    result = concat([pd.Series(x), pd.Series(y)], ignore_index=True)
    tm.assert_series_equal(result, pd.Series(x + y, dtype='object'))
    y = [pd.Period('2011-03', freq='M'), pd.Period('2011-04', freq='M')]
    result = concat([pd.Series(x), pd.Series(y)], ignore_index=True)
    tm.assert_series_equal(result, pd.Series(x + y, dtype='object'))