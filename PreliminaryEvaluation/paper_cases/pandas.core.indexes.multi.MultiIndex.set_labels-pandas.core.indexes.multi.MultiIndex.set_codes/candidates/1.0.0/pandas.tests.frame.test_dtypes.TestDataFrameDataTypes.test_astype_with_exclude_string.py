def test_astype_with_exclude_string(self, float_frame):
    df = float_frame.copy()
    expected = float_frame.astype(int)
    df['string'] = 'foo'
    casted = df.astype(int, errors='ignore')
    expected['string'] = 'foo'
    tm.assert_frame_equal(casted, expected)
    df = float_frame.copy()
    expected = float_frame.astype(np.int32)
    df['string'] = 'foo'
    casted = df.astype(np.int32, errors='ignore')
    expected['string'] = 'foo'
    tm.assert_frame_equal(casted, expected)