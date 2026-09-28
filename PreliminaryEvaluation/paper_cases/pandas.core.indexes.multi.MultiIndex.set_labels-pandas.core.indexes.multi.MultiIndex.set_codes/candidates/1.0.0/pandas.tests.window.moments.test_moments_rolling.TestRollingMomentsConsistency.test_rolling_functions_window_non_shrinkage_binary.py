def test_rolling_functions_window_non_shrinkage_binary(self):
    df = DataFrame([[1, 5], [3, 2], [3, 9], [-1, 0]], columns=Index(['A', 'B'], name='foo'), index=Index(range(4), name='bar'))
    df_expected = DataFrame(columns=Index(['A', 'B'], name='foo'), index=pd.MultiIndex.from_product([df.index, df.columns], names=['bar', 'foo']), dtype='float64')
    functions = [lambda x: x.rolling(window=10, min_periods=5).cov(x, pairwise=True), lambda x: x.rolling(window=10, min_periods=5).corr(x, pairwise=True)]
    for f in functions:
        df_result = f(df)
        tm.assert_frame_equal(df_result, df_expected)