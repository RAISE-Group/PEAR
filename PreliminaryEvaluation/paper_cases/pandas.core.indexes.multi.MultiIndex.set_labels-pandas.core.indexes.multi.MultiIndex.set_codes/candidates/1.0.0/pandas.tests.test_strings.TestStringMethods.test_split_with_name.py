def test_split_with_name(self):
    s = Series(['a,b', 'c,d'], name='xxx')
    res = s.str.split(',')
    exp = Series([['a', 'b'], ['c', 'd']], name='xxx')
    tm.assert_series_equal(res, exp)
    res = s.str.split(',', expand=True)
    exp = DataFrame([['a', 'b'], ['c', 'd']])
    tm.assert_frame_equal(res, exp)
    idx = Index(['a,b', 'c,d'], name='xxx')
    res = idx.str.split(',')
    exp = Index([['a', 'b'], ['c', 'd']], name='xxx')
    assert res.nlevels == 1
    tm.assert_index_equal(res, exp)
    res = idx.str.split(',', expand=True)
    exp = MultiIndex.from_tuples([('a', 'b'), ('c', 'd')])
    assert res.nlevels == 2
    tm.assert_index_equal(res, exp)