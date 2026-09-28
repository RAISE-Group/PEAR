def test_iloc_col(self):
    df = DataFrame(np.random.randn(4, 10), columns=range(0, 20, 2))
    result = df.iloc[:, 1]
    exp = df.loc[:, 2]
    tm.assert_series_equal(result, exp)
    result = df.iloc[:, 2]
    exp = df.loc[:, 4]
    tm.assert_series_equal(result, exp)
    result = df.iloc[:, slice(4, 8)]
    expected = df.loc[:, 8:14]
    tm.assert_frame_equal(result, expected)
    with pytest.raises(com.SettingWithCopyError):
        result[8] = 0.0
    assert (df[8] == 0).all()
    result = df.iloc[:, [1, 2, 4, 6]]
    expected = df.reindex(columns=df.columns[[1, 2, 4, 6]])
    tm.assert_frame_equal(result, expected)