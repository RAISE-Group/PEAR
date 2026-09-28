def test_groupby_transform(self):
    s = self.frame['A']
    grouper = s.index.get_level_values(0)
    grouped = s.groupby(grouper)
    applied = grouped.apply(lambda x: x * 2)
    expected = grouped.transform(lambda x: x * 2)
    result = applied.reindex(expected.index)
    tm.assert_series_equal(result, expected, check_names=False)