def test_stack_unstack_multiple(self):
    unstacked = self.ymd.unstack(['year', 'month'])
    expected = self.ymd.unstack('year').unstack('month')
    tm.assert_frame_equal(unstacked, expected)
    assert unstacked.columns.names == expected.columns.names
    s = self.ymd['A']
    s_unstacked = s.unstack(['year', 'month'])
    tm.assert_frame_equal(s_unstacked, expected['A'])
    restacked = unstacked.stack(['year', 'month'])
    restacked = restacked.swaplevel(0, 1).swaplevel(1, 2)
    restacked = restacked.sort_index(level=0)
    tm.assert_frame_equal(restacked, self.ymd)
    assert restacked.index.names == self.ymd.index.names
    unstacked = self.ymd.unstack([1, 2])
    expected = self.ymd.unstack(1).unstack(1).dropna(axis=1, how='all')
    tm.assert_frame_equal(unstacked, expected)
    unstacked = self.ymd.unstack([2, 1])
    expected = self.ymd.unstack(2).unstack(1).dropna(axis=1, how='all')
    tm.assert_frame_equal(unstacked, expected.loc[:, unstacked.columns])