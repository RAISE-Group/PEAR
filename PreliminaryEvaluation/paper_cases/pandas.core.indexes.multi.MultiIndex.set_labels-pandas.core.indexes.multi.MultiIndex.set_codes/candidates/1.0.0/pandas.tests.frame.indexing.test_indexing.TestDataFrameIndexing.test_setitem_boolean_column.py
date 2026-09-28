def test_setitem_boolean_column(self, float_frame):
    expected = float_frame.copy()
    mask = float_frame['A'] > 0
    float_frame.loc[mask, 'B'] = 0
    expected.values[mask.values, 1] = 0
    tm.assert_frame_equal(float_frame, expected)