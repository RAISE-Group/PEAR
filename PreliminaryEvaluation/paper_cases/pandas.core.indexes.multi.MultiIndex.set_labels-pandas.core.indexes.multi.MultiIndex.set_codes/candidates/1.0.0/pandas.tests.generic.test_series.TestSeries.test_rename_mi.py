def test_rename_mi(self):
    s = Series([11, 21, 31], index=MultiIndex.from_tuples([('A', x) for x in ['a', 'B', 'c']]))
    s.rename(str.lower)