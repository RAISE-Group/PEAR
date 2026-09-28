def test_rank_dense_method(self):
    dtypes = ['O', 'f8', 'i8']
    in_out = [([1], [1]), ([2], [1]), ([0], [1]), ([2, 2], [1, 1]), ([1, 2, 3], [1, 2, 3]), ([4, 2, 1], [3, 2, 1]), ([1, 1, 5, 5, 3], [1, 1, 3, 3, 2]), ([-5, -4, -3, -2, -1], [1, 2, 3, 4, 5])]
    for ser, exp in in_out:
        for dtype in dtypes:
            s = Series(ser).astype(dtype)
            result = s.rank(method='dense')
            expected = Series(exp).astype(result.dtype)
            tm.assert_series_equal(result, expected)