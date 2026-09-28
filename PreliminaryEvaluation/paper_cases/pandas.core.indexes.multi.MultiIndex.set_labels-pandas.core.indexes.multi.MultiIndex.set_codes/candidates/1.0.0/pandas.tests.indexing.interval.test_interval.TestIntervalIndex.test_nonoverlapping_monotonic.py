@pytest.mark.parametrize('direction', ['increasing', 'decreasing'])
def test_nonoverlapping_monotonic(self, direction, closed):
    tpls = [(0, 1), (2, 3), (4, 5)]
    if direction == 'decreasing':
        tpls = tpls[::-1]
    idx = IntervalIndex.from_tuples(tpls, closed=closed)
    s = Series(list('abc'), idx)
    for key, expected in zip(idx.left, s):
        if idx.closed_left:
            assert s[key] == expected
            assert s.loc[key] == expected
        else:
            with pytest.raises(KeyError, match=str(key)):
                s[key]
            with pytest.raises(KeyError, match=str(key)):
                s.loc[key]
    for key, expected in zip(idx.right, s):
        if idx.closed_right:
            assert s[key] == expected
            assert s.loc[key] == expected
        else:
            with pytest.raises(KeyError, match=str(key)):
                s[key]
            with pytest.raises(KeyError, match=str(key)):
                s.loc[key]
    for key, expected in zip(idx.mid, s):
        assert s[key] == expected
        assert s.loc[key] == expected