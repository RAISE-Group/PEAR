def test_multi_iter_frame(self, three_group):
    k1 = np.array(['b', 'b', 'b', 'a', 'a', 'a'])
    k2 = np.array(['1', '2', '1', '2', '1', '2'])
    df = DataFrame({'v1': np.random.randn(6), 'v2': np.random.randn(6), 'k1': k1, 'k2': k2}, index=['one', 'two', 'three', 'four', 'five', 'six'])
    grouped = df.groupby(['k1', 'k2'])
    iterated = list(grouped)
    idx = df.index
    expected = [('a', '1', df.loc[idx[[4]]]), ('a', '2', df.loc[idx[[3, 5]]]), ('b', '1', df.loc[idx[[0, 2]]]), ('b', '2', df.loc[idx[[1]]])]
    for i, ((one, two), three) in enumerate(iterated):
        e1, e2, e3 = expected[i]
        assert e1 == one
        assert e2 == two
        tm.assert_frame_equal(three, e3)
    df['k1'] = np.array(['b', 'b', 'b', 'a', 'a', 'a'])
    df['k2'] = np.array(['1', '1', '1', '2', '2', '2'])
    grouped = df.groupby(['k1', 'k2'])
    groups = {key: gp for key, gp in grouped}
    assert len(groups) == 2
    three_levels = three_group.groupby(['A', 'B', 'C']).mean()
    grouped = three_levels.T.groupby(axis=1, level=(1, 2))
    for key, group in grouped:
        pass