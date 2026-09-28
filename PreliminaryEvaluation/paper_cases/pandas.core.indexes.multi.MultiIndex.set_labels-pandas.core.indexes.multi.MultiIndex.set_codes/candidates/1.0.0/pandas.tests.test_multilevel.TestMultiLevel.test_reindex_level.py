def test_reindex_level(self):
    month_sums = self.ymd.sum(level='month')
    result = month_sums.reindex(self.ymd.index, level=1)
    expected = self.ymd.groupby(level='month').transform(np.sum)
    tm.assert_frame_equal(result, expected)
    result = month_sums['A'].reindex(self.ymd.index, level=1)
    expected = self.ymd['A'].groupby(level='month').transform(np.sum)
    tm.assert_series_equal(result, expected, check_names=False)
    month_sums = self.ymd.T.sum(axis=1, level='month')
    result = month_sums.reindex(columns=self.ymd.index, level=1)
    expected = self.ymd.groupby(level='month').transform(np.sum).T
    tm.assert_frame_equal(result, expected)