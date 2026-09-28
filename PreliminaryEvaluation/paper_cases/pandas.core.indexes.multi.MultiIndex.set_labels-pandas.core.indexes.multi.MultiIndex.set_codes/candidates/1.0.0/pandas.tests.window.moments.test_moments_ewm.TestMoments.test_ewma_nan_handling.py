def test_ewma_nan_handling(self):
    s = Series([1.0] + [np.nan] * 5 + [1.0])
    result = s.ewm(com=5).mean()
    tm.assert_series_equal(result, Series([1.0] * len(s)))
    s = Series([np.nan] * 2 + [1.0] + [np.nan] * 2 + [1.0])
    result = s.ewm(com=5).mean()
    tm.assert_series_equal(result, Series([np.nan] * 2 + [1.0] * 4))
    s0 = Series([np.nan, 1.0, 101.0])
    s1 = Series([1.0, np.nan, 101.0])
    s2 = Series([np.nan, 1.0, np.nan, np.nan, 101.0, np.nan])
    s3 = Series([1.0, np.nan, 101.0, 50.0])
    com = 2.0
    alpha = 1.0 / (1.0 + com)

    def simple_wma(s, w):
        return (s.multiply(w).cumsum() / w.cumsum()).fillna(method='ffill')
    for s, adjust, ignore_na, w in [(s0, True, False, [np.nan, 1.0 - alpha, 1.0]), (s0, True, True, [np.nan, 1.0 - alpha, 1.0]), (s0, False, False, [np.nan, 1.0 - alpha, alpha]), (s0, False, True, [np.nan, 1.0 - alpha, alpha]), (s1, True, False, [(1.0 - alpha) ** 2, np.nan, 1.0]), (s1, True, True, [1.0 - alpha, np.nan, 1.0]), (s1, False, False, [(1.0 - alpha) ** 2, np.nan, alpha]), (s1, False, True, [1.0 - alpha, np.nan, alpha]), (s2, True, False, [np.nan, (1.0 - alpha) ** 3, np.nan, np.nan, 1.0, np.nan]), (s2, True, True, [np.nan, 1.0 - alpha, np.nan, np.nan, 1.0, np.nan]), (s2, False, False, [np.nan, (1.0 - alpha) ** 3, np.nan, np.nan, alpha, np.nan]), (s2, False, True, [np.nan, 1.0 - alpha, np.nan, np.nan, alpha, np.nan]), (s3, True, False, [(1.0 - alpha) ** 3, np.nan, 1.0 - alpha, 1.0]), (s3, True, True, [(1.0 - alpha) ** 2, np.nan, 1.0 - alpha, 1.0]), (s3, False, False, [(1.0 - alpha) ** 3, np.nan, (1.0 - alpha) * alpha, alpha * ((1.0 - alpha) ** 2 + alpha)]), (s3, False, True, [(1.0 - alpha) ** 2, np.nan, (1.0 - alpha) * alpha, alpha])]:
        expected = simple_wma(s, Series(w))
        result = s.ewm(com=com, adjust=adjust, ignore_na=ignore_na).mean()
        tm.assert_series_equal(result, expected)
        if ignore_na is False:
            result = s.ewm(com=com, adjust=adjust).mean()
            tm.assert_series_equal(result, expected)