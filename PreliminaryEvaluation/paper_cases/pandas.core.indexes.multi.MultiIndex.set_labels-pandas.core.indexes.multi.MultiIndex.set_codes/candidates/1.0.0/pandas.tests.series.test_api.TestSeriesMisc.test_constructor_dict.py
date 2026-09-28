def test_constructor_dict(self):
    d = {'a': 0.0, 'b': 1.0, 'c': 2.0}
    result = Series(d)
    expected = Series(d, index=sorted(d.keys()))
    tm.assert_series_equal(result, expected)
    result = Series(d, index=['b', 'c', 'd', 'a'])
    expected = Series([1, 2, np.nan, 0], index=['b', 'c', 'd', 'a'])
    tm.assert_series_equal(result, expected)