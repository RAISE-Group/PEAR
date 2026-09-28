def test_reorder_levels(self):
    result = self.ymd.reorder_levels(['month', 'day', 'year'])
    expected = self.ymd.swaplevel(0, 1).swaplevel(1, 2)
    tm.assert_frame_equal(result, expected)
    result = self.ymd['A'].reorder_levels(['month', 'day', 'year'])
    expected = self.ymd['A'].swaplevel(0, 1).swaplevel(1, 2)
    tm.assert_series_equal(result, expected)
    result = self.ymd.T.reorder_levels(['month', 'day', 'year'], axis=1)
    expected = self.ymd.T.swaplevel(0, 1, axis=1).swaplevel(1, 2, axis=1)
    tm.assert_frame_equal(result, expected)
    with pytest.raises(TypeError, match='hierarchical axis'):
        self.ymd.reorder_levels([1, 2], axis=1)
    with pytest.raises(IndexError, match='Too many levels'):
        self.ymd.index.reorder_levels([1, 2, 3])