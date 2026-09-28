def test_setitem_scalars_no_index(self):
    df = DataFrame()
    df['foo'] = 1
    expected = DataFrame(columns=['foo']).astype(np.int64)
    tm.assert_frame_equal(df, expected)