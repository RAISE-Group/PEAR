def test_iloc_setitem_list_of_lists(self):
    df = DataFrame(dict(A=np.arange(5, dtype='int64'), B=np.arange(5, 10, dtype='int64')))
    df.iloc[2:4] = [[10, 11], [12, 13]]
    expected = DataFrame(dict(A=[0, 1, 10, 12, 4], B=[5, 6, 11, 13, 9]))
    tm.assert_frame_equal(df, expected)
    df = DataFrame(dict(A=list('abcde'), B=np.arange(5, 10, dtype='int64')))
    df.iloc[2:4] = [['x', 11], ['y', 13]]
    expected = DataFrame(dict(A=['a', 'b', 'x', 'y', 'e'], B=[5, 6, 11, 13, 9]))
    tm.assert_frame_equal(df, expected)