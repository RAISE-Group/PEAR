def test_concat_series_axis1(self, sort=sort):
    ts = tm.makeTimeSeries()
    pieces = [ts[:-2], ts[2:], ts[2:-2]]
    result = concat(pieces, axis=1)
    expected = DataFrame(pieces).T
    tm.assert_frame_equal(result, expected)
    result = concat(pieces, keys=['A', 'B', 'C'], axis=1)
    expected = DataFrame(pieces, index=['A', 'B', 'C']).T
    tm.assert_frame_equal(result, expected)
    s = Series(randn(5), name='A')
    s2 = Series(randn(5), name='B')
    result = concat([s, s2], axis=1)
    expected = DataFrame({'A': s, 'B': s2})
    tm.assert_frame_equal(result, expected)
    s2.name = None
    result = concat([s, s2], axis=1)
    tm.assert_index_equal(result.columns, Index(['A', 0], dtype='object'))
    s = Series(randn(3), index=['c', 'a', 'b'], name='A')
    s2 = Series(randn(4), index=['d', 'a', 'b', 'c'], name='B')
    result = concat([s, s2], axis=1, sort=sort)
    expected = DataFrame({'A': s, 'B': s2})
    tm.assert_frame_equal(result, expected)