def test_sort_index_level_by_name(self):
    self.frame.index.names = ['first', 'second']
    result = self.frame.sort_index(level='second')
    expected = self.frame.sort_index(level=1)
    tm.assert_frame_equal(result, expected)