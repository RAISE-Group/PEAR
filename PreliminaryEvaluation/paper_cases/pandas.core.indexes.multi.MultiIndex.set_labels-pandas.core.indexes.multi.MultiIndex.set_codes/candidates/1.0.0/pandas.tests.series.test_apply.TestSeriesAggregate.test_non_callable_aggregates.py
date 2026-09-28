def test_non_callable_aggregates(self):
    s = Series([1, 2, None])
    result = s.agg('size')
    expected = s.size
    assert result == expected
    result = s.agg(['size', 'count', 'mean'])
    expected = Series({'size': 3.0, 'count': 2.0, 'mean': 1.5})
    tm.assert_series_equal(result[expected.index], expected)