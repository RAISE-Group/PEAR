def test_groupby_multilevel(self):
    result = self.ymd.groupby(level=[0, 1]).mean()
    k1 = self.ymd.index.get_level_values(0)
    k2 = self.ymd.index.get_level_values(1)
    expected = self.ymd.groupby([k1, k2]).mean()
    tm.assert_frame_equal(result, expected, check_names=False)
    assert result.index.names == self.ymd.index.names[:2]
    result2 = self.ymd.groupby(level=self.ymd.index.names[:2]).mean()
    tm.assert_frame_equal(result, result2)