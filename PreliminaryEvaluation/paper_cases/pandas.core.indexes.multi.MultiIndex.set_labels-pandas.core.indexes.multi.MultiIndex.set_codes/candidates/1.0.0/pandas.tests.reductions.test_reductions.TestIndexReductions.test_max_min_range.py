@pytest.mark.parametrize('start,stop,step', [(0, 400, 3), (500, 0, -6), (-10 ** 6, 10 ** 6, 4), (10 ** 6, -10 ** 6, -4), (0, 10, 20)])
def test_max_min_range(self, start, stop, step):
    idx = RangeIndex(start, stop, step)
    expected = idx._int64index.max()
    result = idx.max()
    assert result == expected
    result2 = idx.max(skipna=False)
    assert result2 == expected
    expected = idx._int64index.min()
    result = idx.min()
    assert result == expected
    result2 = idx.min(skipna=False)
    assert result2 == expected
    idx = RangeIndex(start, stop, -step)
    assert isna(idx.max())
    assert isna(idx.min())