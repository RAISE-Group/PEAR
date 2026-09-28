def test_dataframe_constructor(self):
    multi = DataFrame(np.random.randn(4, 4), index=[np.array(['a', 'a', 'b', 'b']), np.array(['x', 'y', 'x', 'y'])])
    assert isinstance(multi.index, MultiIndex)
    assert not isinstance(multi.columns, MultiIndex)
    multi = DataFrame(np.random.randn(4, 4), columns=[['a', 'a', 'b', 'b'], ['x', 'y', 'x', 'y']])
    assert isinstance(multi.columns, MultiIndex)