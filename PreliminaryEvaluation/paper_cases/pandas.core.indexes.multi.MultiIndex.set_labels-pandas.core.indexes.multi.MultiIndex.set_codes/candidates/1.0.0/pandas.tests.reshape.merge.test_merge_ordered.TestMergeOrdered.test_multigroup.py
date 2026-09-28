def test_multigroup(self):
    left = pd.concat([self.left, self.left], ignore_index=True)
    left['group'] = ['a'] * 3 + ['b'] * 3
    result = merge_ordered(left, self.right, on='key', left_by='group', fill_method='ffill')
    expected = DataFrame({'key': ['a', 'b', 'c', 'd', 'e', 'f'] * 2, 'lvalue': [1.0, 1, 2, 2, 3, 3.0] * 2, 'rvalue': [np.nan, 1, 2, 3, 3, 4] * 2})
    expected['group'] = ['a'] * 6 + ['b'] * 6
    tm.assert_frame_equal(result, expected.loc[:, result.columns])
    result2 = merge_ordered(self.right, left, on='key', right_by='group', fill_method='ffill')
    tm.assert_frame_equal(result, result2.loc[:, result.columns])
    result = merge_ordered(left, self.right, on='key', left_by='group')
    assert result['group'].notna().all()