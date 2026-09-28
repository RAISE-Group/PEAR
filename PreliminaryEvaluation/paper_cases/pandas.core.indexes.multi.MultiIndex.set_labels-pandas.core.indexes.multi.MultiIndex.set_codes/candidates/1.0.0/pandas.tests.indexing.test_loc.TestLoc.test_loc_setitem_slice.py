def test_loc_setitem_slice(self):
    df1 = DataFrame({'a': [0, 1, 1], 'b': Series([100, 200, 300], dtype='uint32')})
    ix = df1['a'] == 1
    newb1 = df1.loc[ix, 'b'] + 1
    df1.loc[ix, 'b'] = newb1
    expected = DataFrame({'a': [0, 1, 1], 'b': Series([100, 201, 301], dtype='uint32')})
    tm.assert_frame_equal(df1, expected)
    df2 = DataFrame({'a': [0, 1, 1], 'b': [100, 200, 300]}, dtype='uint64')
    ix = df1['a'] == 1
    newb2 = df2.loc[ix, 'b']
    df1.loc[ix, 'b'] = newb2
    expected = DataFrame({'a': [0, 1, 1], 'b': [100, 200, 300]}, dtype='uint64')
    tm.assert_frame_equal(df2, expected)