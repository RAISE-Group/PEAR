def test_examples1(self):
    """ doc-string examples """
    left = pd.DataFrame({'a': [1, 5, 10], 'left_val': ['a', 'b', 'c']})
    right = pd.DataFrame({'a': [1, 2, 3, 6, 7], 'right_val': [1, 2, 3, 6, 7]})
    expected = pd.DataFrame({'a': [1, 5, 10], 'left_val': ['a', 'b', 'c'], 'right_val': [1, 3, 7]})
    result = pd.merge_asof(left, right, on='a')
    tm.assert_frame_equal(result, expected)