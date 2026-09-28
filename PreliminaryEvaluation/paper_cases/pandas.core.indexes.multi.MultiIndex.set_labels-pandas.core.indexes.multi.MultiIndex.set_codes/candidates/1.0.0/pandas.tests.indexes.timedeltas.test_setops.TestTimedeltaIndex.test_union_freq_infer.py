def test_union_freq_infer(self):
    tdi = pd.timedelta_range('1 Day', periods=5)
    left = tdi[[0, 1, 3, 4]]
    right = tdi[[2, 3, 1]]
    assert left.freq is None
    assert right.freq is None
    result = left.union(right)
    tm.assert_index_equal(result, tdi)
    assert result.freq == 'D'