def test_rename_axis_inplace(self, float_frame):
    expected = float_frame.rename_axis('foo')
    result = float_frame.copy()
    no_return = result.rename_axis('foo', inplace=True)
    assert no_return is None
    tm.assert_frame_equal(result, expected)
    expected = float_frame.rename_axis('bar', axis=1)
    result = float_frame.copy()
    no_return = result.rename_axis('bar', axis=1, inplace=True)
    assert no_return is None
    tm.assert_frame_equal(result, expected)