def test_sort_index_level(self):
    df = self.frame.copy()
    df.index = np.arange(len(df))
    a_sorted = self.frame['A'].sort_index(level=0)
    assert a_sorted.index.names == self.frame.index.names
    rs = self.frame.copy()
    rs.sort_index(level=0, inplace=True)
    tm.assert_frame_equal(rs, self.frame.sort_index(level=0))