def test_4d_ndarray_fails(self):
    x = randn(3, 4, 5, 6)
    y = Series(randn(10))
    with pytest.raises(NotImplementedError):
        self.eval('x + y', local_dict={'x': x, 'y': y})