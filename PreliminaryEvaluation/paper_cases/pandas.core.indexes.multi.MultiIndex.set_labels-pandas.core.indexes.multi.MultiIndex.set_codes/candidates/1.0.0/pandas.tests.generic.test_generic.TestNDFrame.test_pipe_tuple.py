def test_pipe_tuple(self):
    df = DataFrame({'A': [1, 2, 3]})
    f = lambda x, y: y
    result = df.pipe((f, 'y'), 0)
    tm.assert_frame_equal(result, df)
    result = df.A.pipe((f, 'y'), 0)
    tm.assert_series_equal(result, df.A)