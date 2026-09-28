def test_datetime_count(self):
    df = DataFrame({'a': [1, 2, 3] * 2, 'dates': pd.date_range('now', periods=6, freq='T')})
    result = df.groupby('a').dates.count()
    expected = Series([2, 2, 2], index=Index([1, 2, 3], name='a'), name='dates')
    tm.assert_series_equal(result, expected)