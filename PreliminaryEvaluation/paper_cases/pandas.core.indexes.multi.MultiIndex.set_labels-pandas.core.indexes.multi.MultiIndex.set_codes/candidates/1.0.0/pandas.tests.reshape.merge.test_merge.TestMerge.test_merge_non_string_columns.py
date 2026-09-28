def test_merge_non_string_columns(self):
    left = pd.DataFrame({0: [1, 0, 1, 0], 1: [0, 1, 0, 0], 2: [0, 0, 2, 0], 3: [1, 0, 0, 3]})
    right = left.astype(float)
    expected = left
    result = pd.merge(left, right)
    tm.assert_frame_equal(expected, result)