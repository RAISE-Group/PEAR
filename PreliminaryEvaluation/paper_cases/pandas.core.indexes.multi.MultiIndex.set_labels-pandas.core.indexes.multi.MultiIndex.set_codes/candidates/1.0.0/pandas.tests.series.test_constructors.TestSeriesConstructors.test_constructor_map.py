def test_constructor_map(self):
    m = map(lambda x: x, range(10))
    result = Series(m)
    exp = Series(range(10))
    tm.assert_series_equal(result, exp)
    m = map(lambda x: x, range(10))
    result = Series(m, index=range(10, 20))
    exp.index = range(10, 20)
    tm.assert_series_equal(result, exp)