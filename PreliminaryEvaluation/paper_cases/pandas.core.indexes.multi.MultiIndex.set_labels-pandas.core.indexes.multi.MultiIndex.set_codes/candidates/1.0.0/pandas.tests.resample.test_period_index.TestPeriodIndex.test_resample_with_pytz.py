def test_resample_with_pytz(self):
    s = Series(2, index=pd.date_range('2017-01-01', periods=48, freq='H', tz='US/Eastern'))
    result = s.resample('D').mean()
    expected = Series(2, index=pd.DatetimeIndex(['2017-01-01', '2017-01-02'], tz='US/Eastern'))
    tm.assert_series_equal(result, expected)
    assert result.index.tz == pytz.timezone('US/Eastern')