def test_sort_index_level_mixed(self):
    sorted_before = self.frame.sort_index(level=1)
    df = self.frame.copy()
    df['foo'] = 'bar'
    sorted_after = df.sort_index(level=1)
    tm.assert_frame_equal(sorted_before, sorted_after.drop(['foo'], axis=1))
    dft = self.frame.T
    sorted_before = dft.sort_index(level=1, axis=1)
    dft['foo', 'three'] = 'bar'
    sorted_after = dft.sort_index(level=1, axis=1)
    tm.assert_frame_equal(sorted_before.drop([('foo', 'three')], axis=1), sorted_after.drop([('foo', 'three')], axis=1))