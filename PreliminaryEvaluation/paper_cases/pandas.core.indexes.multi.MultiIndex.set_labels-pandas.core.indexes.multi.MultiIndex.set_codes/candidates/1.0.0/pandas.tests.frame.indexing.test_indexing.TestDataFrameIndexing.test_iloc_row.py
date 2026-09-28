def test_iloc_row(self):
    df = DataFrame(np.random.randn(10, 4), index=range(0, 20, 2))
    result = df.iloc[1]
    exp = df.loc[2]
    tm.assert_series_equal(result, exp)
    result = df.iloc[2]
    exp = df.loc[4]
    tm.assert_series_equal(result, exp)
    result = df.iloc[slice(4, 8)]
    expected = df.loc[8:14]
    tm.assert_frame_equal(result, expected)
    with pytest.raises(com.SettingWithCopyError):
        result[2] = 0.0
    exp_col = df[2].copy()
    exp_col[4:8] = 0.0
    tm.assert_series_equal(df[2], exp_col)
    result = df.iloc[[1, 2, 4, 6]]
    expected = df.reindex(df.index[[1, 2, 4, 6]])
    tm.assert_frame_equal(result, expected)