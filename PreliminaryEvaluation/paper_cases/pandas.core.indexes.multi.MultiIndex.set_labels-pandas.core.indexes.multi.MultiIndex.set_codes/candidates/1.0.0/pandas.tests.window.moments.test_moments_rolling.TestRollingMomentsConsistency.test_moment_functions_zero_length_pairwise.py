def test_moment_functions_zero_length_pairwise(self):
    df1 = DataFrame()
    df2 = DataFrame(columns=Index(['a'], name='foo'), index=Index([], name='bar'))
    df2['a'] = df2['a'].astype('float64')
    df1_expected = DataFrame(index=pd.MultiIndex.from_product([df1.index, df1.columns]), columns=Index([]))
    df2_expected = DataFrame(index=pd.MultiIndex.from_product([df2.index, df2.columns], names=['bar', 'foo']), columns=Index(['a'], name='foo'), dtype='float64')
    functions = [lambda x: x.rolling(window=10, min_periods=5).cov(x, pairwise=True), lambda x: x.rolling(window=10, min_periods=5).corr(x, pairwise=True)]
    for f in functions:
        df1_result = f(df1)
        tm.assert_frame_equal(df1_result, df1_expected)
        df2_result = f(df2)
        tm.assert_frame_equal(df2_result, df2_expected)