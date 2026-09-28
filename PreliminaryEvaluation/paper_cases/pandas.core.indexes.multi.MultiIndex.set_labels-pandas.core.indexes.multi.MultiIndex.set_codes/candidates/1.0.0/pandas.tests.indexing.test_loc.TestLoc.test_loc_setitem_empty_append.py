def test_loc_setitem_empty_append(self):
    data = [1, 2, 3]
    expected = DataFrame({'x': data, 'y': [None] * len(data)})
    df = DataFrame(columns=['x', 'y'])
    df.loc[:, 'x'] = data
    tm.assert_frame_equal(df, expected)
    expected = DataFrame({'x': [1.0], 'y': [np.nan]})
    df = DataFrame(columns=['x', 'y'], dtype=np.float)
    df.loc[0, 'x'] = expected.loc[0, 'x']
    tm.assert_frame_equal(df, expected)