def test_clip_with_na_args(self, float_frame):
    """Should process np.nan argument as None """
    tm.assert_frame_equal(float_frame.clip(np.nan), float_frame)
    tm.assert_frame_equal(float_frame.clip(upper=np.nan, lower=np.nan), float_frame)
    df = DataFrame({'col_0': [1, 2, 3], 'col_1': [4, 5, 6], 'col_2': [7, 8, 9]})
    result = df.clip(lower=[4, 5, np.nan], axis=0)
    expected = DataFrame({'col_0': [4, 5, np.nan], 'col_1': [4, 5, np.nan], 'col_2': [7, 8, np.nan]})
    tm.assert_frame_equal(result, expected)
    result = df.clip(lower=[4, 5, np.nan], axis=1)
    expected = DataFrame({'col_0': [4, 4, 4], 'col_1': [5, 5, 6], 'col_2': [np.nan, np.nan, np.nan]})
    tm.assert_frame_equal(result, expected)