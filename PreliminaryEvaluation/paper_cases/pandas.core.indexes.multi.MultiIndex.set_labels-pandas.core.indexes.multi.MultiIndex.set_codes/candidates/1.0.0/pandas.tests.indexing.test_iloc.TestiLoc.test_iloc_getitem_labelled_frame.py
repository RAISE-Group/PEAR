def test_iloc_getitem_labelled_frame(self):
    df = DataFrame(np.random.randn(10, 4), index=list('abcdefghij'), columns=list('ABCD'))
    result = df.iloc[1, 1]
    exp = df.loc['b', 'B']
    assert result == exp
    result = df.iloc[:, 2:3]
    expected = df.loc[:, ['C']]
    tm.assert_frame_equal(result, expected)
    result = df.iloc[-1, -1]
    exp = df.loc['j', 'D']
    assert result == exp
    msg = 'single positional indexer is out-of-bounds'
    with pytest.raises(IndexError, match=msg):
        df.iloc[10, 5]
    msg = 'Location based indexing can only have \\[integer, integer slice \\(START point is INCLUDED, END point is EXCLUDED\\), listlike of integers, boolean array\\] types'
    with pytest.raises(ValueError, match=msg):
        df.iloc['j', 'D']