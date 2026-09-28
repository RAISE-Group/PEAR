def test_float_index_non_scalar_assignment(self):
    df = DataFrame({'a': [1, 2, 3], 'b': [3, 4, 5]}, index=[1.0, 2.0, 3.0])
    df.loc[df.index[:2]] = 1
    expected = DataFrame({'a': [1, 1, 3], 'b': [1, 1, 5]}, index=df.index)
    tm.assert_frame_equal(expected, df)
    df = DataFrame({'a': [1, 2, 3], 'b': [3, 4, 5]}, index=[1.0, 2.0, 3.0])
    df2 = df.copy()
    df.loc[df.index] = df.loc[df.index]
    tm.assert_frame_equal(df, df2)