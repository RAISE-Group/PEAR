def test_with_datetimelikes(self):
    df = DataFrame({'A': date_range('20130101', periods=10), 'B': timedelta_range('1 day', periods=10)})
    t = df.T
    result = t.dtypes.value_counts()
    expected = Series({np.dtype('object'): 10})
    tm.assert_series_equal(result, expected)