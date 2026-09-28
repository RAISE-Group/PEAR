def test_corrwith_dup_cols(self):
    df1 = pd.DataFrame(np.vstack([np.arange(10)] * 3).T)
    df2 = df1.copy()
    df2 = pd.concat((df2, df2[0]), axis=1)
    result = df1.corrwith(df2)
    expected = pd.Series(np.ones(4), index=[0, 0, 1, 2])
    tm.assert_series_equal(result, expected)