def test_frame_loc_callable_labels(self):
    df = pd.DataFrame({'X': [1, 2, 3, 4], 'Y': list('aabb')}, index=list('ABCD'))
    res = df.loc[lambda x: ['A', 'C']]
    tm.assert_frame_equal(res, df.loc[['A', 'C']])
    res = df.loc[lambda x: ['A', 'C'],]
    tm.assert_frame_equal(res, df.loc[['A', 'C'],])
    res = df.loc[lambda x: ['A', 'C'], :]
    tm.assert_frame_equal(res, df.loc[['A', 'C'], :])
    res = df.loc[lambda x: ['A', 'C'], lambda x: 'X']
    tm.assert_series_equal(res, df.loc[['A', 'C'], 'X'])
    res = df.loc[lambda x: ['A', 'C'], lambda x: ['X']]
    tm.assert_frame_equal(res, df.loc[['A', 'C'], ['X']])
    res = df.loc[['A', 'C'], lambda x: 'X']
    tm.assert_series_equal(res, df.loc[['A', 'C'], 'X'])
    res = df.loc[['A', 'C'], lambda x: ['X']]
    tm.assert_frame_equal(res, df.loc[['A', 'C'], ['X']])
    res = df.loc[lambda x: ['A', 'C'], 'X']
    tm.assert_series_equal(res, df.loc[['A', 'C'], 'X'])
    res = df.loc[lambda x: ['A', 'C'], ['X']]
    tm.assert_frame_equal(res, df.loc[['A', 'C'], ['X']])