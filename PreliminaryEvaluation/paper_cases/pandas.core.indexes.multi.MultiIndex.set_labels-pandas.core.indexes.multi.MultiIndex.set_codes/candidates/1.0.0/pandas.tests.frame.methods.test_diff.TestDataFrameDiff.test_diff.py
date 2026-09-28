def test_diff(self, datetime_frame):
    the_diff = datetime_frame.diff(1)
    tm.assert_series_equal(the_diff['A'], datetime_frame['A'] - datetime_frame['A'].shift(1))
    a = 10000000000000000
    b = a + 1
    s = Series([a, b])
    rs = DataFrame({'s': s}).diff()
    assert rs.s[1] == 1
    tf = datetime_frame.astype('float32')
    the_diff = tf.diff(1)
    tm.assert_series_equal(the_diff['A'], tf['A'] - tf['A'].shift(1))
    df = pd.DataFrame({'y': pd.Series([2]), 'z': pd.Series([3])})
    df.insert(0, 'x', 1)
    result = df.diff(axis=1)
    expected = pd.DataFrame({'x': np.nan, 'y': pd.Series(1), 'z': pd.Series(1)}).astype('float64')
    tm.assert_frame_equal(result, expected)