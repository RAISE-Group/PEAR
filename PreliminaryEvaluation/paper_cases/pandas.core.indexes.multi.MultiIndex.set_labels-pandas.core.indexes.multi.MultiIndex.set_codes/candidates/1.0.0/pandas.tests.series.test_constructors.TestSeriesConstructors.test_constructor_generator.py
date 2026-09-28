def test_constructor_generator(self):
    gen = (i for i in range(10))
    result = Series(gen)
    exp = Series(range(10))
    tm.assert_series_equal(result, exp)
    gen = (i for i in range(10))
    result = Series(gen, index=range(10, 20))
    exp.index = range(10, 20)
    tm.assert_series_equal(result, exp)