def test_apply_with_reduce_empty(self):
    empty_frame = DataFrame()
    x = []
    result = empty_frame.apply(x.append, axis=1, result_type='expand')
    tm.assert_frame_equal(result, empty_frame)
    result = empty_frame.apply(x.append, axis=1, result_type='reduce')
    expected = Series([], index=pd.Index([], dtype=object), dtype=np.float64)
    tm.assert_series_equal(result, expected)
    empty_with_cols = DataFrame(columns=['a', 'b', 'c'])
    result = empty_with_cols.apply(x.append, axis=1, result_type='expand')
    tm.assert_frame_equal(result, empty_with_cols)
    result = empty_with_cols.apply(x.append, axis=1, result_type='reduce')
    expected = Series([], index=pd.Index([], dtype=object), dtype=np.float64)
    tm.assert_series_equal(result, expected)
    assert x == []