def test_getitem_setitem_boolean_misaligned(self, float_frame):
    mask = float_frame['A'][::-1] > 1
    result = float_frame.loc[mask]
    expected = float_frame.loc[mask[::-1]]
    tm.assert_frame_equal(result, expected)
    cp = float_frame.copy()
    expected = float_frame.copy()
    cp.loc[mask] = 0
    expected.loc[mask] = 0
    tm.assert_frame_equal(cp, expected)