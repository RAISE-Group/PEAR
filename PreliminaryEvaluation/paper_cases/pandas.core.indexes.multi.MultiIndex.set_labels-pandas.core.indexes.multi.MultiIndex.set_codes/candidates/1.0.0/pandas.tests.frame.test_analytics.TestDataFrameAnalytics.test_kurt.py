@td.skip_if_no_scipy
def test_kurt(self):
    index = MultiIndex(levels=[['bar'], ['one', 'two', 'three'], [0, 1]], codes=[[0, 0, 0, 0, 0, 0], [0, 1, 2, 0, 1, 2], [0, 1, 0, 1, 0, 1]])
    df = DataFrame(np.random.randn(6, 3), index=index)
    kurt = df.kurt()
    kurt2 = df.kurt(level=0).xs('bar')
    tm.assert_series_equal(kurt, kurt2, check_names=False)
    assert kurt.name is None
    assert kurt2.name == 'bar'