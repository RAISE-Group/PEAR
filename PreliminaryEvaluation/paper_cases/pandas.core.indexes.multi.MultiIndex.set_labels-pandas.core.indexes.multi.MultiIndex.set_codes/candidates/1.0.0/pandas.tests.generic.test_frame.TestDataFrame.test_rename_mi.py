def test_rename_mi(self):
    df = DataFrame([11, 21, 31], index=MultiIndex.from_tuples([('A', x) for x in ['a', 'B', 'c']]))
    df.rename(str.lower)