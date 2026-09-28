def test_empty_str_methods_to_frame(self):
    empty = Series(dtype=str)
    empty_df = DataFrame()
    tm.assert_frame_equal(empty_df, empty.str.partition('a'))
    tm.assert_frame_equal(empty_df, empty.str.rpartition('a'))