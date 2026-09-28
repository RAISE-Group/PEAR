def test_ffill(self):
    result = merge_ordered(self.left, self.right, on='key', fill_method='ffill')
    expected = DataFrame({'key': ['a', 'b', 'c', 'd', 'e', 'f'], 'lvalue': [1.0, 1, 2, 2, 3, 3.0], 'rvalue': [np.nan, 1, 2, 3, 3, 4]})
    tm.assert_frame_equal(result, expected)