def test_join_multi_multi(self, left_multi, right_multi, join_type, on_cols_multi, idx_cols_multi):
    expected = pd.merge(left_multi.reset_index(), right_multi.reset_index(), how=join_type, on=on_cols_multi).set_index(idx_cols_multi).sort_index()
    result = left_multi.join(right_multi, how=join_type).sort_index()
    tm.assert_frame_equal(result, expected)