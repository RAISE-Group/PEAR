def test_series_constructor(self):
    multi = Series(1.0, index=[np.array(['a', 'a', 'b', 'b']), np.array(['x', 'y', 'x', 'y'])])
    assert isinstance(multi.index, MultiIndex)
    multi = Series(1.0, index=[['a', 'a', 'b', 'b'], ['x', 'y', 'x', 'y']])
    assert isinstance(multi.index, MultiIndex)
    multi = Series(range(4), index=[['a', 'a', 'b', 'b'], ['x', 'y', 'x', 'y']])
    assert isinstance(multi.index, MultiIndex)