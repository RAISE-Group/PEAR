@pytest.mark.parametrize('sort', [False, True])
def test_merge_right_vs_left(self, left, right, sort):
    on_cols = ['key1', 'key2']
    merged_left_right = left.merge(right, left_on=on_cols, right_index=True, how='left', sort=sort)
    merge_right_left = right.merge(left, right_on=on_cols, left_index=True, how='right', sort=sort)
    merge_right_left = merge_right_left[merged_left_right.columns]
    tm.assert_frame_equal(merged_left_right, merge_right_left)