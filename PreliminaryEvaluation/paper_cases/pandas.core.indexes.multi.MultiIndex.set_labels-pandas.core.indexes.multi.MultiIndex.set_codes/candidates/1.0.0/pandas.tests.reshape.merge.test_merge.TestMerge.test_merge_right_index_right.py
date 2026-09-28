def test_merge_right_index_right(self):
    left = pd.DataFrame({'a': [1, 2, 3], 'key': [0, 1, 1]})
    right = pd.DataFrame({'b': [1, 2, 3]})
    expected = pd.DataFrame({'a': [1, 2, 3, None], 'key': [0, 1, 1, 2], 'b': [1, 2, 2, 3]}, columns=['a', 'key', 'b'], index=[0, 1, 2, np.nan])
    result = left.merge(right, left_on='key', right_index=True, how='right')
    tm.assert_frame_equal(result, expected)