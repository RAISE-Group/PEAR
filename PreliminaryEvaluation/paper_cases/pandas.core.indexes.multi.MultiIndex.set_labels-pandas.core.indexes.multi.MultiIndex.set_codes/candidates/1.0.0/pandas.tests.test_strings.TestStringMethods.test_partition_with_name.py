def test_partition_with_name(self):
    s = Series(['a,b', 'c,d'], name='xxx')
    res = s.str.partition(',')
    exp = DataFrame({0: ['a', 'c'], 1: [',', ','], 2: ['b', 'd']})
    tm.assert_frame_equal(res, exp)
    res = s.str.partition(',', expand=False)
    exp = Series([('a', ',', 'b'), ('c', ',', 'd')], name='xxx')
    tm.assert_series_equal(res, exp)
    idx = Index(['a,b', 'c,d'], name='xxx')
    res = idx.str.partition(',')
    exp = MultiIndex.from_tuples([('a', ',', 'b'), ('c', ',', 'd')])
    assert res.nlevels == 3
    tm.assert_index_equal(res, exp)
    res = idx.str.partition(',', expand=False)
    exp = Index(np.array([('a', ',', 'b'), ('c', ',', 'd')]), name='xxx')
    assert res.nlevels == 1
    tm.assert_index_equal(res, exp)