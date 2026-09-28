def test_cummethods_bool(self):
    a = pd.Series([False, False, False, True, True, False, False])
    b = ~a
    c = pd.Series([False] * len(b))
    d = ~c
    methods = {'cumsum': np.cumsum, 'cumprod': np.cumprod, 'cummin': np.minimum.accumulate, 'cummax': np.maximum.accumulate}
    args = product((a, b, c, d), methods)
    for s, method in args:
        expected = pd.Series(methods[method](s.values))
        result = getattr(s, method)()
        tm.assert_series_equal(result, expected)
    e = pd.Series([False, True, np.nan, False])
    cse = pd.Series([0, 1, np.nan, 1], dtype=object)
    cpe = pd.Series([False, 0, np.nan, 0])
    cmin = pd.Series([False, False, np.nan, False])
    cmax = pd.Series([False, True, np.nan, True])
    expecteds = {'cumsum': cse, 'cumprod': cpe, 'cummin': cmin, 'cummax': cmax}
    for method in methods:
        res = getattr(e, method)()
        tm.assert_series_equal(res, expecteds[method])