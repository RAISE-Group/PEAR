def test_non_callable_aggregates(self):
    df = DataFrame({'A': [None, 2, 3], 'B': [1.0, np.nan, 3.0], 'C': ['foo', None, 'bar']})
    result = df.agg({'A': 'count'})
    expected = Series({'A': 2})
    tm.assert_series_equal(result, expected)
    result = df.agg({'A': 'size'})
    expected = Series({'A': 3})
    tm.assert_series_equal(result, expected)
    result1 = df.agg(['count', 'size'])
    result2 = df.agg({'A': ['count', 'size'], 'B': ['count', 'size'], 'C': ['count', 'size']})
    expected = pd.DataFrame({'A': {'count': 2, 'size': 3}, 'B': {'count': 2, 'size': 3}, 'C': {'count': 2, 'size': 3}})
    tm.assert_frame_equal(result1, result2, check_like=True)
    tm.assert_frame_equal(result2, expected, check_like=True)
    result = df.agg('count')
    expected = df.count()
    tm.assert_series_equal(result, expected)
    result = df.agg('size')
    expected = df.size
    assert result == expected