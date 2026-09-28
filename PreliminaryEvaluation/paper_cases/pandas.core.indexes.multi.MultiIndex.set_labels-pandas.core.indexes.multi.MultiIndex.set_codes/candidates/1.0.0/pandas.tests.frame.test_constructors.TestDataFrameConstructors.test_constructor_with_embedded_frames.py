def test_constructor_with_embedded_frames(self):
    df1 = DataFrame({'a': [1, 2, 3], 'b': [3, 4, 5]})
    df2 = DataFrame([df1, df1 + 10])
    df2.dtypes
    str(df2)
    result = df2.loc[0, 0]
    tm.assert_frame_equal(result, df1)
    result = df2.loc[1, 0]
    tm.assert_frame_equal(result, df1 + 10)