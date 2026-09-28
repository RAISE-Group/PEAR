@pytest.mark.parametrize('f', [lambda x: x.rolling(window=10, min_periods=5).cov(x, pairwise=False), lambda x: x.rolling(window=10, min_periods=5).corr(x, pairwise=False), lambda x: x.rolling(window=10, min_periods=5).max(), lambda x: x.rolling(window=10, min_periods=5).min(), lambda x: x.rolling(window=10, min_periods=5).sum(), lambda x: x.rolling(window=10, min_periods=5).mean(), lambda x: x.rolling(window=10, min_periods=5).std(), lambda x: x.rolling(window=10, min_periods=5).var(), lambda x: x.rolling(window=10, min_periods=5).skew(), lambda x: x.rolling(window=10, min_periods=5).kurt(), lambda x: x.rolling(window=10, min_periods=5).quantile(quantile=0.5), lambda x: x.rolling(window=10, min_periods=5).median(), lambda x: x.rolling(window=10, min_periods=5).apply(sum, raw=False), lambda x: x.rolling(window=10, min_periods=5).apply(sum, raw=True), lambda x: x.rolling(win_type='boxcar', window=10, min_periods=5).mean()])
@td.skip_if_no_scipy
def test_rolling_functions_window_non_shrinkage(self, f):
    s = Series(range(4))
    s_expected = Series(np.nan, index=s.index)
    df = DataFrame([[1, 5], [3, 2], [3, 9], [-1, 0]], columns=['A', 'B'])
    df_expected = DataFrame(np.nan, index=df.index, columns=df.columns)
    s_result = f(s)
    tm.assert_series_equal(s_result, s_expected)
    df_result = f(df)
    tm.assert_frame_equal(df_result, df_expected)