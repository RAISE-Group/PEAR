def test_ragged_min(self):
    df = self.ragged
    result = df.rolling(window='1s', min_periods=1).min()
    expected = df.copy()
    expected['B'] = [0.0, 1, 2, 3, 4]
    tm.assert_frame_equal(result, expected)
    result = df.rolling(window='2s', min_periods=1).min()
    expected = df.copy()
    expected['B'] = [0.0, 1, 1, 3, 3]
    tm.assert_frame_equal(result, expected)
    result = df.rolling(window='5s', min_periods=1).min()
    expected = df.copy()
    expected['B'] = [0.0, 0, 0, 1, 1]
    tm.assert_frame_equal(result, expected)