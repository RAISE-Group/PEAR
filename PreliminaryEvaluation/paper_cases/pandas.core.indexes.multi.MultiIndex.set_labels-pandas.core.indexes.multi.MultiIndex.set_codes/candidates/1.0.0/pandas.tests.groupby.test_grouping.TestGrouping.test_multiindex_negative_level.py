def test_multiindex_negative_level(self, mframe):
    result = mframe.groupby(level=-1).sum()
    expected = mframe.groupby(level='second').sum()
    tm.assert_frame_equal(result, expected)
    result = mframe.groupby(level=-2).sum()
    expected = mframe.groupby(level='first').sum()
    tm.assert_frame_equal(result, expected)
    result = mframe.groupby(level=[-2, -1]).sum()
    expected = mframe
    tm.assert_frame_equal(result, expected)
    result = mframe.groupby(level=[-1, 'first']).sum()
    expected = mframe.groupby(level=['second', 'first']).sum()
    tm.assert_frame_equal(result, expected)