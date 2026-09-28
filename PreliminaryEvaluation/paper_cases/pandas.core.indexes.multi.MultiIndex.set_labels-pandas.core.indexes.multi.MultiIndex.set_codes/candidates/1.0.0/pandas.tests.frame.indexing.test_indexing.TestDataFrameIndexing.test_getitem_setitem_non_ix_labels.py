def test_getitem_setitem_non_ix_labels(self):
    df = tm.makeTimeDataFrame()
    start, end = df.index[[5, 10]]
    result = df.loc[start:end]
    result2 = df[start:end]
    expected = df[5:11]
    tm.assert_frame_equal(result, expected)
    tm.assert_frame_equal(result2, expected)
    result = df.copy()
    result.loc[start:end] = 0
    result2 = df.copy()
    result2[start:end] = 0
    expected = df.copy()
    expected[5:11] = 0
    tm.assert_frame_equal(result, expected)
    tm.assert_frame_equal(result2, expected)