def test_array_interface(self, float_frame):
    with np.errstate(all='ignore'):
        result = np.sqrt(float_frame)
    assert isinstance(result, type(float_frame))
    assert result.index is float_frame.index
    assert result.columns is float_frame.columns
    tm.assert_frame_equal(result, float_frame.apply(np.sqrt))