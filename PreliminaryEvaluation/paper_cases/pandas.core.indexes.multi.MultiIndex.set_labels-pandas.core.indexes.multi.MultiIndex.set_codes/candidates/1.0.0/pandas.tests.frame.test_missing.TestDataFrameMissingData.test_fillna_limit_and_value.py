def test_fillna_limit_and_value(self):
    df = DataFrame(np.random.randn(10, 3))
    df.iloc[2:7, 0] = np.nan
    df.iloc[3:5, 2] = np.nan
    expected = df.copy()
    expected.iloc[2, 0] = 999
    expected.iloc[3, 2] = 999
    result = df.fillna(999, limit=1)
    tm.assert_frame_equal(result, expected)