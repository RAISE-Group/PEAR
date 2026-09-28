@pytest.mark.parametrize('klass', [list, tuple, np.array, Series])
def test_where(self, closed, klass):
    idx = self.create_index(closed=closed)
    cond = [True] * len(idx)
    expected = idx
    result = expected.where(klass(cond))
    tm.assert_index_equal(result, expected)
    cond = [False] + [True] * len(idx[1:])
    expected = IntervalIndex([np.nan] + idx[1:].tolist())
    result = idx.where(klass(cond))
    tm.assert_index_equal(result, expected)