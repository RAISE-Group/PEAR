def test_rolling_axis_count(self, axis_frame):
    df = DataFrame({'x': range(3), 'y': range(3)})
    axis = df._get_axis_number(axis_frame)
    if axis in [0, 'index']:
        expected = DataFrame({'x': [1.0, 2.0, 2.0], 'y': [1.0, 2.0, 2.0]})
    else:
        expected = DataFrame({'x': [1.0, 1.0, 1.0], 'y': [2.0, 2.0, 2.0]})
    result = df.rolling(2, axis=axis_frame, min_periods=0).count()
    tm.assert_frame_equal(result, expected)