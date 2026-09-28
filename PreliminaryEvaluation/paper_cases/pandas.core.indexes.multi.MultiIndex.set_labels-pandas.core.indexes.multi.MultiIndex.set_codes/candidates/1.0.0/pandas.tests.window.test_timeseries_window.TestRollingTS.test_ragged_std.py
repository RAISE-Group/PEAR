def test_ragged_std(self):
    df = self.ragged
    result = df.rolling(window='1s', min_periods=1).std(ddof=0)
    expected = df.copy()
    expected['B'] = [0.0] * 5
    tm.assert_frame_equal(result, expected)
    result = df.rolling(window='1s', min_periods=1).std(ddof=1)
    expected = df.copy()
    expected['B'] = [np.nan] * 5
    tm.assert_frame_equal(result, expected)
    result = df.rolling(window='3s', min_periods=1).std(ddof=0)
    expected = df.copy()
    expected['B'] = [0.0] + [0.5] * 4
    tm.assert_frame_equal(result, expected)
    result = df.rolling(window='5s', min_periods=1).std(ddof=1)
    expected = df.copy()
    expected['B'] = [np.nan, 0.707107, 1.0, 1.0, 1.290994]
    tm.assert_frame_equal(result, expected)