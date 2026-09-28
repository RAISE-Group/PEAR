def test_partial_setting(self):
    s_orig = Series([1, 2, 3])
    s = s_orig.copy()
    s[5] = 5
    expected = Series([1, 2, 3, 5], index=[0, 1, 2, 5])
    tm.assert_series_equal(s, expected)
    s = s_orig.copy()
    s.loc[5] = 5
    expected = Series([1, 2, 3, 5], index=[0, 1, 2, 5])
    tm.assert_series_equal(s, expected)
    s = s_orig.copy()
    s[5] = 5.0
    expected = Series([1, 2, 3, 5.0], index=[0, 1, 2, 5])
    tm.assert_series_equal(s, expected)
    s = s_orig.copy()
    s.loc[5] = 5.0
    expected = Series([1, 2, 3, 5.0], index=[0, 1, 2, 5])
    tm.assert_series_equal(s, expected)
    s = s_orig.copy()
    with pytest.raises(IndexError):
        s.iloc[3] = 5.0
    with pytest.raises(IndexError):
        s.iat[3] = 5.0
    df_orig = DataFrame(np.arange(6).reshape(3, 2), columns=['A', 'B'], dtype='int64')
    df = df_orig.copy()
    with pytest.raises(IndexError):
        df.iloc[4, 2] = 5.0
    with pytest.raises(IndexError):
        df.iat[4, 2] = 5.0
    expected = DataFrame(dict({'A': [0, 4, 4], 'B': [1, 5, 5]}))
    df = df_orig.copy()
    df.iloc[1] = df.iloc[2]
    tm.assert_frame_equal(df, expected)
    expected = DataFrame(dict({'A': [0, 4, 4], 'B': [1, 5, 5]}))
    df = df_orig.copy()
    df.loc[1] = df.loc[2]
    tm.assert_frame_equal(df, expected)
    expected = DataFrame(dict({'A': [0, 2, 4, 4], 'B': [1, 3, 5, 5]}))
    df = df_orig.copy()
    df.loc[3] = df.loc[2]
    tm.assert_frame_equal(df, expected)
    expected = DataFrame(dict({'A': [0, 2, 4], 'B': [0, 2, 4]}))
    df = df_orig.copy()
    df.loc[:, 'B'] = df.loc[:, 'A']
    tm.assert_frame_equal(df, expected)
    expected = DataFrame(dict({'A': [0, 2, 4], 'B': Series([0, 2, 4])}))
    df = df_orig.copy()
    df['B'] = df['B'].astype(np.float64)
    df.loc[:, 'B'] = df.loc[:, 'A']
    tm.assert_frame_equal(df, expected)
    expected = df_orig.copy()
    expected['C'] = df['A']
    df = df_orig.copy()
    df.loc[:, 'C'] = df.loc[:, 'A']
    tm.assert_frame_equal(df, expected)
    expected = df_orig.copy()
    expected['C'] = df['A']
    df = df_orig.copy()
    df.loc[:, 'C'] = df.loc[:, 'A']
    tm.assert_frame_equal(df, expected)
    dates = date_range('1/1/2000', periods=8)
    df_orig = DataFrame(np.random.randn(8, 4), index=dates, columns=['A', 'B', 'C', 'D'])
    expected = pd.concat([df_orig, DataFrame({'A': 7}, index=[dates[-1] + dates.freq])], sort=True)
    df = df_orig.copy()
    df.loc[dates[-1] + dates.freq, 'A'] = 7
    tm.assert_frame_equal(df, expected)
    df = df_orig.copy()
    df.at[dates[-1] + dates.freq, 'A'] = 7
    tm.assert_frame_equal(df, expected)
    exp_other = DataFrame({0: 7}, index=[dates[-1] + dates.freq])
    expected = pd.concat([df_orig, exp_other], axis=1)
    df = df_orig.copy()
    df.loc[dates[-1] + dates.freq, 0] = 7
    tm.assert_frame_equal(df, expected)
    df = df_orig.copy()
    df.at[dates[-1] + dates.freq, 0] = 7
    tm.assert_frame_equal(df, expected)