def test_drop_level(self):
    result = self.frame.drop(['bar', 'qux'], level='first')
    expected = self.frame.iloc[[0, 1, 2, 5, 6]]
    tm.assert_frame_equal(result, expected)
    result = self.frame.drop(['two'], level='second')
    expected = self.frame.iloc[[0, 2, 3, 6, 7, 9]]
    tm.assert_frame_equal(result, expected)
    result = self.frame.T.drop(['bar', 'qux'], axis=1, level='first')
    expected = self.frame.iloc[[0, 1, 2, 5, 6]].T
    tm.assert_frame_equal(result, expected)
    result = self.frame.T.drop(['two'], axis=1, level='second')
    expected = self.frame.iloc[[0, 2, 3, 6, 7, 9]].T
    tm.assert_frame_equal(result, expected)