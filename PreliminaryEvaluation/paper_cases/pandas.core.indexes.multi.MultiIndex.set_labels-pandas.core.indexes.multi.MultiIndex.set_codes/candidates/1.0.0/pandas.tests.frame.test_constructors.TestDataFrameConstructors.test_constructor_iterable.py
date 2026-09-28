def test_constructor_iterable(self):

    class Iter:

        def __iter__(self):
            for i in range(10):
                yield [1, 2, 3]
    expected = DataFrame([[1, 2, 3]] * 10)
    result = DataFrame(Iter())
    tm.assert_frame_equal(result, expected)