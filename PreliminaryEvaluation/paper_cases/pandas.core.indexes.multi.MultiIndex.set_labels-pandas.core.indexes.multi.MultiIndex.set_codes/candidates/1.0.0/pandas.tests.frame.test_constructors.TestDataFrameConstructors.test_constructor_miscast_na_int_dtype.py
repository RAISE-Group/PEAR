def test_constructor_miscast_na_int_dtype(self):
    df = DataFrame([[np.nan, 1], [1, 0]], dtype=np.int64)
    expected = DataFrame([[np.nan, 1], [1, 0]])
    tm.assert_frame_equal(df, expected)