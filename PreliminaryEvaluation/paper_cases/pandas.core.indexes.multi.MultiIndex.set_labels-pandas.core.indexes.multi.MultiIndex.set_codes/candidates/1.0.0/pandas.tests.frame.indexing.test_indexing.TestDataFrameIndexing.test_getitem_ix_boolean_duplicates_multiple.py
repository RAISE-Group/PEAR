def test_getitem_ix_boolean_duplicates_multiple(self):
    df = DataFrame(np.random.randn(5, 3), index=['foo', 'foo', 'bar', 'baz', 'bar'])
    result = df.loc[['bar']]
    exp = df.iloc[[2, 4]]
    tm.assert_frame_equal(result, exp)
    result = df.loc[df[1] > 0]
    exp = df[df[1] > 0]
    tm.assert_frame_equal(result, exp)
    result = df.loc[df[0] > 0]
    exp = df[df[0] > 0]
    tm.assert_frame_equal(result, exp)