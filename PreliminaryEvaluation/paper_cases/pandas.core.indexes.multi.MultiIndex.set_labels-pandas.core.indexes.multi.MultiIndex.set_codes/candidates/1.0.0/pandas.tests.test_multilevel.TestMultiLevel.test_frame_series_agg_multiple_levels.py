def test_frame_series_agg_multiple_levels(self):
    result = self.ymd.sum(level=['year', 'month'])
    expected = self.ymd.groupby(level=['year', 'month']).sum()
    tm.assert_frame_equal(result, expected)
    result = self.ymd['A'].sum(level=['year', 'month'])
    expected = self.ymd['A'].groupby(level=['year', 'month']).sum()
    tm.assert_series_equal(result, expected)