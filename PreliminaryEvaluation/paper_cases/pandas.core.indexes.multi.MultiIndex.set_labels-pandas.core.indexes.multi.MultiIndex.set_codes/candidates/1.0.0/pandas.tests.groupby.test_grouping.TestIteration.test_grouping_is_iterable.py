def test_grouping_is_iterable(self, tsframe):
    grouped = tsframe.groupby([lambda x: x.weekday(), lambda x: x.year])
    for g in grouped.grouper.groupings[0]:
        pass