def test_ngroup_respects_groupby_order(self):
    np.random.seed(0)
    df = DataFrame({'a': np.random.choice(list('abcdef'), 100)})
    for sort_flag in (False, True):
        g = df.groupby(['a'], sort=sort_flag)
        df['group_id'] = -1
        df['group_index'] = -1
        for i, (_, group) in enumerate(g):
            df.loc[group.index, 'group_id'] = i
            for j, ind in enumerate(group.index):
                df.loc[ind, 'group_index'] = j
        tm.assert_series_equal(Series(df['group_id'].values), g.ngroup())
        tm.assert_series_equal(Series(df['group_index'].values), g.cumcount())