def test_floating_tuples(self):
    s = Series([(1, 1), (2, 2), (3, 3)], index=[0.0, 0.1, 0.2], name='foo')
    result = s[0.0]
    assert result == (1, 1)
    expected = Series([(1, 1), (2, 2)], index=[0.0, 0.0], name='foo')
    s = Series([(1, 1), (2, 2), (3, 3)], index=[0.0, 0.0, 0.2], name='foo')
    result = s[0.0]
    tm.assert_series_equal(result, expected)