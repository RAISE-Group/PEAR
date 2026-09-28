@pytest.mark.parametrize('level', ['A', 0])
def test_sort_index_multiindex(self, level):
    mi = MultiIndex.from_tuples([[1, 1, 3], [1, 1, 1]], names=list('ABC'))
    s = Series([1, 2], mi)
    backwards = s.iloc[[1, 0]]
    res = s.sort_index(level=level)
    tm.assert_series_equal(backwards, res)
    res = s.sort_index(level=level, sort_remaining=False)
    tm.assert_series_equal(s, res)