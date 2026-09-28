def test_non_monotonic(self):
    dates = date_range(start='2016-01-01 09:30:00', periods=20, freq='s')
    df = DataFrame({'A': [1] * 20 + [2] * 12 + [3] * 8, 'B': np.concatenate((dates, dates)), 'C': np.arange(40)})
    result = df.groupby('A').rolling('4s', on='B').C.mean()
    expected = df.set_index('B').groupby('A').apply(lambda x: x.rolling('4s')['C'].mean())
    tm.assert_series_equal(result, expected)
    df2 = df.sort_values('B')
    result = df2.groupby('A').rolling('4s', on='B').C.mean()
    tm.assert_series_equal(result, expected)