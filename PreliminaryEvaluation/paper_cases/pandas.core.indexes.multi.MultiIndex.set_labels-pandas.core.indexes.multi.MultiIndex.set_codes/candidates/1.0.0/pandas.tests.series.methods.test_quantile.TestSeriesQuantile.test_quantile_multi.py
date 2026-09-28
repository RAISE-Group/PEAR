def test_quantile_multi(self, datetime_series):
    qs = [0.1, 0.9]
    result = datetime_series.quantile(qs)
    expected = pd.Series([np.percentile(datetime_series.dropna(), 10), np.percentile(datetime_series.dropna(), 90)], index=qs, name=datetime_series.name)
    tm.assert_series_equal(result, expected)
    dts = datetime_series.index.to_series()
    dts.name = 'xxx'
    result = dts.quantile((0.2, 0.2))
    expected = Series([Timestamp('2000-01-10 19:12:00'), Timestamp('2000-01-10 19:12:00')], index=[0.2, 0.2], name='xxx')
    tm.assert_series_equal(result, expected)
    result = datetime_series.quantile([])
    expected = pd.Series([], name=datetime_series.name, index=Index([], dtype=float), dtype='float64')
    tm.assert_series_equal(result, expected)