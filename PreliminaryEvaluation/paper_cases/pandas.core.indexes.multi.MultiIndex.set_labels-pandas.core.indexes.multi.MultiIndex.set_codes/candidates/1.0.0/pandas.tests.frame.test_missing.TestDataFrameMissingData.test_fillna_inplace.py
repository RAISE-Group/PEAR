def test_fillna_inplace(self):
    df = DataFrame(np.random.randn(10, 4))
    df[1][:4] = np.nan
    df[3][-4:] = np.nan
    expected = df.fillna(value=0)
    assert expected is not df
    df.fillna(value=0, inplace=True)
    tm.assert_frame_equal(df, expected)
    expected = df.fillna(value={0: 0}, inplace=True)
    assert expected is None
    df[1][:4] = np.nan
    df[3][-4:] = np.nan
    expected = df.fillna(method='ffill')
    assert expected is not df
    df.fillna(method='ffill', inplace=True)
    tm.assert_frame_equal(df, expected)