def test_missing_minp_zero_variable(self):
    x = pd.Series([np.nan] * 4, index=pd.DatetimeIndex(['2017-01-01', '2017-01-04', '2017-01-06', '2017-01-07']))
    result = x.rolling(pd.Timedelta('2d'), min_periods=0).sum()
    expected = pd.Series(0.0, index=x.index)
    tm.assert_series_equal(result, expected)