def test_constructor_dict_order(self):
    d = {'b': 1, 'a': 0, 'c': 2}
    result = Series(d)
    expected = Series([1, 0, 2], index=list('bac'))
    tm.assert_series_equal(result, expected)