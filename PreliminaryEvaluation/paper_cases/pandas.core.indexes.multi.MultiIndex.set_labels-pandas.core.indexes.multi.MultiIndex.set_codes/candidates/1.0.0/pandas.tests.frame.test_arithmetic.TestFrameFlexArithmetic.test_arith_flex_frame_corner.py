def test_arith_flex_frame_corner(self, float_frame):
    const_add = float_frame.add(1)
    tm.assert_frame_equal(const_add, float_frame + 1)
    result = float_frame.add(float_frame[:0])
    tm.assert_frame_equal(result, float_frame * np.nan)
    result = float_frame[:0].add(float_frame)
    tm.assert_frame_equal(result, float_frame * np.nan)
    with pytest.raises(NotImplementedError, match='fill_value'):
        float_frame.add(float_frame.iloc[0], fill_value=3)
    with pytest.raises(NotImplementedError, match='fill_value'):
        float_frame.add(float_frame.iloc[0], axis='index', fill_value=3)