def test_reindex(self):
    expected = self.frame.iloc[[0, 3]]
    reindexed = self.frame.loc[[('foo', 'one'), ('bar', 'one')]]
    tm.assert_frame_equal(reindexed, expected)