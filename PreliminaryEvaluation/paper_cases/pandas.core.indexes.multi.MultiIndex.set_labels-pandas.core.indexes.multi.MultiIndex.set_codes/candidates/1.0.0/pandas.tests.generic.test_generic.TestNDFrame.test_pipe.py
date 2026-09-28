def test_pipe(self):
    df = DataFrame({'A': [1, 2, 3]})
    f = lambda x, y: x ** y
    result = df.pipe(f, 2)
    expected = DataFrame({'A': [1, 4, 9]})
    tm.assert_frame_equal(result, expected)
    result = df.A.pipe(f, 2)
    tm.assert_series_equal(result, expected.A)