def test_groupby_datetime64_32_bit(self):
    df = DataFrame({'A': range(2), 'B': [pd.Timestamp('2000-01-1')] * 2})
    result = df.groupby('A')['B'].transform(min)
    expected = Series([pd.Timestamp('2000-01-1')] * 2, name='B')
    tm.assert_series_equal(result, expected)