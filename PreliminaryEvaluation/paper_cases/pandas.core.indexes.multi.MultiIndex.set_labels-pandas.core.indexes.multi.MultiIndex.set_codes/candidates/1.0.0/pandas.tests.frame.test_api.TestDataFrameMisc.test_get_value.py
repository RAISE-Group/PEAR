def test_get_value(self, float_frame):
    for idx in float_frame.index:
        for col in float_frame.columns:
            result = float_frame._get_value(idx, col)
            expected = float_frame[col][idx]
            tm.assert_almost_equal(result, expected)