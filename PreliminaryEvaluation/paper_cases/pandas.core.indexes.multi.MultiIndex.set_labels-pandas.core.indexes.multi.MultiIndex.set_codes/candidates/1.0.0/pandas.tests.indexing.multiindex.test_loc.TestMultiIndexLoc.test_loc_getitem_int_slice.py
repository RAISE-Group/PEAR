def test_loc_getitem_int_slice(self):
    index = MultiIndex.from_product([[6, 7, 8], ['a', 'b']])
    df = DataFrame(np.random.randn(6, 6), index, index)
    result = df.loc[6:8, :]
    expected = df
    tm.assert_frame_equal(result, expected)
    index = MultiIndex.from_product([[10, 20, 30], ['a', 'b']])
    df = DataFrame(np.random.randn(6, 6), index, index)
    result = df.loc[20:30, :]
    expected = df.iloc[2:]
    tm.assert_frame_equal(result, expected)
    result = df.loc[10, :]
    expected = df.iloc[0:2]
    expected.index = ['a', 'b']
    tm.assert_frame_equal(result, expected)
    result = df.loc[:, 10]
    expected = df[10]
    tm.assert_frame_equal(result, expected)