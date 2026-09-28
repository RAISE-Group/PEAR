def test_partial_boolean_frame_indexing(self):
    df = DataFrame(np.arange(9.0).reshape(3, 3), index=list('abc'), columns=list('ABC'))
    index_df = DataFrame(1, index=list('ab'), columns=list('AB'))
    result = df[index_df.notnull()]
    expected = DataFrame(np.array([[0.0, 1.0, np.nan], [3.0, 4.0, np.nan], [np.nan] * 3]), index=list('abc'), columns=list('ABC'))
    tm.assert_frame_equal(result, expected)