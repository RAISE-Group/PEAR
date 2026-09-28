def test_moment_functions_zero_length(self):
    s = Series(dtype=np.float64)
    s_expected = s
    df1 = DataFrame()
    df1_expected = df1
    df2 = DataFrame(columns=['a'])
    df2['a'] = df2['a'].astype('float64')
    df2_expected = df2
    functions = [lambda x: x.rolling(window=10).count(), lambda x: x.rolling(window=10, min_periods=5).cov(x, pairwise=False), lambda x: x.rolling(window=10, min_periods=5).corr(x, pairwise=False), lambda x: x.rolling(window=10, min_periods=5).max(), lambda x: x.rolling(window=10, min_periods=5).min(), lambda x: x.rolling(window=10, min_periods=5).sum(), lambda x: x.rolling(window=10, min_periods=5).mean(), lambda x: x.rolling(window=10, min_periods=5).std(), lambda x: x.rolling(window=10, min_periods=5).var(), lambda x: x.rolling(window=10, min_periods=5).skew(), lambda x: x.rolling(window=10, min_periods=5).kurt(), lambda x: x.rolling(window=10, min_periods=5).quantile(0.5), lambda x: x.rolling(window=10, min_periods=5).median(), lambda x: x.rolling(window=10, min_periods=5).apply(sum, raw=False), lambda x: x.rolling(window=10, min_periods=5).apply(sum, raw=True), lambda x: x.rolling(win_type='boxcar', window=10, min_periods=5).mean()]
    for f in functions:
        try:
            s_result = f(s)
            tm.assert_series_equal(s_result, s_expected)
            df1_result = f(df1)
            tm.assert_frame_equal(df1_result, df1_expected)
            df2_result = f(df2)
            tm.assert_frame_equal(df2_result, df2_expected)
        except ImportError:
            continue