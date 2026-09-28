def test_union_coverage(self):
    idx = TimedeltaIndex(['3d', '1d', '2d'])
    ordered = TimedeltaIndex(idx.sort_values(), freq='infer')
    result = ordered.union(idx)
    tm.assert_index_equal(result, ordered)
    result = ordered[:0].union(ordered)
    tm.assert_index_equal(result, ordered)
    assert result.freq == ordered.freq