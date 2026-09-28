def test_ragged_max(self):
    df = self.ragged
    result = df.rolling(window='1s', min_periods=1).max()
    expected = df.copy()
    expected['B'] = [0.0, 1, 2, 3, 4]
    tm.assert_frame_equal(result, expected)
    result = df.rolling(window='2s', min_periods=1).max()
    expected = df.copy()
    expected['B'] = [0.0, 1, 2, 3, 4]
    tm.assert_frame_equal(result, expected)
    result = df.rolling(window='5s', min_periods=1).max()
    expected = df.copy()
    expected['B'] = [0.0, 1, 2, 3, 4]
    tm.assert_frame_equal(result, expected)