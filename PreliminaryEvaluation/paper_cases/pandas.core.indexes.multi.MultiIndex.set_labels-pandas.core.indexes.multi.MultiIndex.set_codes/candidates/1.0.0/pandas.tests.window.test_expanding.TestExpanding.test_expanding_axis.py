def test_expanding_axis(self, axis_frame):
    df = DataFrame(np.ones((10, 20)))
    axis = df._get_axis_number(axis_frame)
    if axis == 0:
        expected = DataFrame({i: [np.nan] * 2 + [float(j) for j in range(3, 11)] for i in range(20)})
    else:
        expected = DataFrame([[np.nan] * 2 + [float(i) for i in range(3, 21)]] * 10)
    result = df.expanding(3, axis=axis_frame).sum()
    tm.assert_frame_equal(result, expected)