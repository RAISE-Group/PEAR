def test_apply_box(self):
    vals = [pd.Timestamp('2011-01-01'), pd.Timestamp('2011-01-02')]
    s = pd.Series(vals)
    assert s.dtype == 'datetime64[ns]'
    res = s.apply(lambda x: f'{type(x).__name__}_{x.day}_{x.tz}')
    exp = pd.Series(['Timestamp_1_None', 'Timestamp_2_None'])
    tm.assert_series_equal(res, exp)
    vals = [pd.Timestamp('2011-01-01', tz='US/Eastern'), pd.Timestamp('2011-01-02', tz='US/Eastern')]
    s = pd.Series(vals)
    assert s.dtype == 'datetime64[ns, US/Eastern]'
    res = s.apply(lambda x: f'{type(x).__name__}_{x.day}_{x.tz}')
    exp = pd.Series(['Timestamp_1_US/Eastern', 'Timestamp_2_US/Eastern'])
    tm.assert_series_equal(res, exp)
    vals = [pd.Timedelta('1 days'), pd.Timedelta('2 days')]
    s = pd.Series(vals)
    assert s.dtype == 'timedelta64[ns]'
    res = s.apply(lambda x: f'{type(x).__name__}_{x.days}')
    exp = pd.Series(['Timedelta_1', 'Timedelta_2'])
    tm.assert_series_equal(res, exp)
    vals = [pd.Period('2011-01-01', freq='M'), pd.Period('2011-01-02', freq='M')]
    s = pd.Series(vals)
    assert s.dtype == 'Period[M]'
    res = s.apply(lambda x: f'{type(x).__name__}_{x.freqstr}')
    exp = pd.Series(['Period_M', 'Period_M'])
    tm.assert_series_equal(res, exp)