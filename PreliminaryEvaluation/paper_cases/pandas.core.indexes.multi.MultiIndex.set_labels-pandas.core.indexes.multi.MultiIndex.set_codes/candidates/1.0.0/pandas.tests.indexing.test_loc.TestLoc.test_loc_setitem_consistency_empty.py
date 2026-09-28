def test_loc_setitem_consistency_empty(self):
    expected = DataFrame(columns=['x', 'y'])
    expected['x'] = expected['x'].astype(np.int64)
    df = DataFrame(columns=['x', 'y'])
    df.loc[:, 'x'] = 1
    tm.assert_frame_equal(df, expected)
    df = DataFrame(columns=['x', 'y'])
    df['x'] = 1
    tm.assert_frame_equal(df, expected)