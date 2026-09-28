def test_reindex_level_partial_selection(self):
    result = self.frame.reindex(['foo', 'qux'], level=0)
    expected = self.frame.iloc[[0, 1, 2, 7, 8, 9]]
    tm.assert_frame_equal(result, expected)
    result = self.frame.T.reindex(['foo', 'qux'], axis=1, level=0)
    tm.assert_frame_equal(result, expected.T)
    result = self.frame.loc[['foo', 'qux']]
    tm.assert_frame_equal(result, expected)
    result = self.frame['A'].loc[['foo', 'qux']]
    tm.assert_series_equal(result, expected['A'])
    result = self.frame.T.loc[:, ['foo', 'qux']]
    tm.assert_frame_equal(result, expected.T)