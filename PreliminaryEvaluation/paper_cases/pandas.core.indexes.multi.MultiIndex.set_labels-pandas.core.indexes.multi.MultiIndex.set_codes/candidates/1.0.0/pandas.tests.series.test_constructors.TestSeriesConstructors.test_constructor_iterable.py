def test_constructor_iterable(self):

    class Iter:

        def __iter__(self):
            for i in range(10):
                yield i
    expected = Series(list(range(10)), dtype='int64')
    result = Series(Iter(), dtype='int64')
    tm.assert_series_equal(result, expected)