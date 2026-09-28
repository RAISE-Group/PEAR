def test_groups(self, df):
    grouped = df.groupby(['A'])
    groups = grouped.groups
    assert groups is grouped.groups
    for k, v in grouped.groups.items():
        assert (df.loc[v]['A'] == k).all()
    grouped = df.groupby(['A', 'B'])
    groups = grouped.groups
    assert groups is grouped.groups
    for k, v in grouped.groups.items():
        assert (df.loc[v]['A'] == k[0]).all()
        assert (df.loc[v]['B'] == k[1]).all()