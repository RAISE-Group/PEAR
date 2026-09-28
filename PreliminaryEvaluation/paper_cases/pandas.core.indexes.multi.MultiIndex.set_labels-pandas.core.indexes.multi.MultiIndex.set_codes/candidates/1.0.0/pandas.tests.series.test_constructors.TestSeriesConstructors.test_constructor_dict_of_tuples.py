def test_constructor_dict_of_tuples(self):
    data = {(1, 2): 3, (None, 5): 6}
    result = Series(data).sort_values()
    expected = Series([3, 6], index=MultiIndex.from_tuples([(1, 2), (None, 5)]))
    tm.assert_series_equal(result, expected)