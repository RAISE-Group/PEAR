@pytest.mark.parametrize('name', [None, 'foo'])
@pytest.mark.parametrize('args, kwargs, start, stop, step', [((5,), dict(), 0, 5, 1), ((1, 5), dict(), 1, 5, 1), ((1, 5, 2), dict(), 1, 5, 2), ((0,), dict(), 0, 0, 1), ((0, 0), dict(), 0, 0, 1), (tuple(), dict(start=0), 0, 0, 1), (tuple(), dict(stop=0), 0, 0, 1)])
def test_constructor(self, args, kwargs, start, stop, step, name):
    result = RangeIndex(*args, name=name, **kwargs)
    expected = Index(np.arange(start, stop, step, dtype=np.int64), name=name)
    assert isinstance(result, RangeIndex)
    assert result.name is name
    assert result._range == range(start, stop, step)
    tm.assert_index_equal(result, expected)