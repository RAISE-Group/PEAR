def test_pivot_with_interval_index(self, interval_values, dropna):
    df = DataFrame({'A': interval_values, 'B': 1})
    result = df.pivot_table(index='A', values='B', dropna=dropna)
    expected = DataFrame({'B': 1}, index=Index(interval_values.unique(), name='A'))
    tm.assert_frame_equal(result, expected)