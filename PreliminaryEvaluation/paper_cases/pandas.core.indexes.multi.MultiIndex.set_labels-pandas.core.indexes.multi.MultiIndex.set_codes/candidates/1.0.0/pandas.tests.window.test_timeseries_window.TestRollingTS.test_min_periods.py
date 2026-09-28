def test_min_periods(self):
    df = self.regular
    expected = df.rolling(2, min_periods=1).sum()
    result = df.rolling('2s').sum()
    tm.assert_frame_equal(result, expected)
    expected = df.rolling(2, min_periods=1).sum()
    result = df.rolling('2s', min_periods=1).sum()
    tm.assert_frame_equal(result, expected)