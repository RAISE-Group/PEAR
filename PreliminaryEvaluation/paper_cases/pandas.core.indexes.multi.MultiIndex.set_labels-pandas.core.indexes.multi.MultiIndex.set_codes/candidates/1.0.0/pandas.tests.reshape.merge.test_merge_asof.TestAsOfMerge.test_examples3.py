def test_examples3(self):
    """ doc-string examples """
    left = pd.DataFrame({'a': [1, 5, 10], 'left_val': ['a', 'b', 'c']})
    right = pd.DataFrame({'a': [1, 2, 3, 6, 7], 'right_val': [1, 2, 3, 6, 7]})
    expected = pd.DataFrame({'a': [1, 5, 10], 'left_val': ['a', 'b', 'c'], 'right_val': [1, 6, np.nan]})
    result = pd.merge_asof(left, right, on='a', direction='forward')
    tm.assert_frame_equal(result, expected)