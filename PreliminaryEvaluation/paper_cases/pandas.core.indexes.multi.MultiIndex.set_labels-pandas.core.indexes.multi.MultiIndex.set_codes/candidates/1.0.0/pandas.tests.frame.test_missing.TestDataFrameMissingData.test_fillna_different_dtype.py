def test_fillna_different_dtype(self):
    df = DataFrame([['a', 'a', np.nan, 'a'], ['b', 'b', np.nan, 'b'], ['c', 'c', np.nan, 'c']])
    result = df.fillna({2: 'foo'})
    expected = DataFrame([['a', 'a', 'foo', 'a'], ['b', 'b', 'foo', 'b'], ['c', 'c', 'foo', 'c']])
    tm.assert_frame_equal(result, expected)
    df.fillna({2: 'foo'}, inplace=True)
    tm.assert_frame_equal(df, expected)