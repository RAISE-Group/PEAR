def test_pipe_tuple_error(self):
    df = DataFrame({'A': [1, 2, 3]})
    f = lambda x, y: y
    with pytest.raises(ValueError):
        df.pipe((f, 'y'), x=1, y=0)
    with pytest.raises(ValueError):
        df.A.pipe((f, 'y'), x=1, y=0)