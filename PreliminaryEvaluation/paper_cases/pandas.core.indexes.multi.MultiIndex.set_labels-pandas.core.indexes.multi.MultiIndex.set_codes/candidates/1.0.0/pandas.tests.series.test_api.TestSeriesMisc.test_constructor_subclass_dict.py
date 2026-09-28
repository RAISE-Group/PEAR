def test_constructor_subclass_dict(self, dict_subclass):
    data = dict_subclass(((x, 10.0 * x) for x in range(10)))
    series = Series(data)
    expected = Series(dict(data.items()))
    tm.assert_series_equal(series, expected)