def test_frame_loc_callable_mixture(self):
    df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': list('aabb'), 'C': [1, 2, 3, 4]})
    res = df.loc[lambda x: x.A > 2, ['A', 'B']]
    tm.assert_frame_equal(res, df.loc[df.A > 2, ['A', 'B']])
    res = df.loc[lambda x: x.A > 2, ['A', 'B']]
    tm.assert_frame_equal(res, df.loc[df.A > 2, ['A', 'B']])
    res = df.loc[[2, 3], lambda x: ['A', 'B']]
    tm.assert_frame_equal(res, df.loc[[2, 3], ['A', 'B']])
    res = df.loc[[2, 3], lambda x: ['A', 'B']]
    tm.assert_frame_equal(res, df.loc[[2, 3], ['A', 'B']])
    res = df.loc[3, lambda x: ['A', 'B']]
    tm.assert_series_equal(res, df.loc[3, ['A', 'B']])
    res = df.loc[3, lambda x: ['A', 'B']]
    tm.assert_series_equal(res, df.loc[3, ['A', 'B']])