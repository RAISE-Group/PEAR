def test_count_level_series(self):
    index = MultiIndex(levels=[['foo', 'bar', 'baz'], ['one', 'two', 'three', 'four']], codes=[[0, 0, 0, 2, 2], [2, 0, 1, 1, 2]])
    s = Series(np.random.randn(len(index)), index=index)
    result = s.count(level=0)
    expected = s.groupby(level=0).count()
    tm.assert_series_equal(result.astype('f8'), expected.reindex(result.index).fillna(0))
    result = s.count(level=1)
    expected = s.groupby(level=1).count()
    tm.assert_series_equal(result.astype('f8'), expected.reindex(result.index).fillna(0))