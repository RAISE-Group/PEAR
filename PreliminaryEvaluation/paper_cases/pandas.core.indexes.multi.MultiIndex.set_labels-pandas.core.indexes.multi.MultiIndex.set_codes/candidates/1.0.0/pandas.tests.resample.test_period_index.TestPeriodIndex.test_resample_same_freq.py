def test_resample_same_freq(self, resample_method):
    series = Series(range(3), index=pd.period_range(start='2000', periods=3, freq='M'))
    expected = series
    result = getattr(series.resample('M'), resample_method)()
    tm.assert_series_equal(result, expected)