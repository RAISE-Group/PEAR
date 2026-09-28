def test_merge_on_multikey(self, left, right, join_type):
    on_cols = ['key1', 'key2']
    result = left.join(right, on=on_cols, how=join_type).reset_index(drop=True)
    expected = pd.merge(left, right.reset_index(), on=on_cols, how=join_type)
    tm.assert_frame_equal(result, expected)
    result = left.join(right, on=on_cols, how=join_type, sort=True).reset_index(drop=True)
    expected = pd.merge(left, right.reset_index(), on=on_cols, how=join_type, sort=True)
    tm.assert_frame_equal(result, expected)