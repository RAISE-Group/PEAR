def test_set_index_cast(self):
    df = DataFrame({'A': [1.1, 2.2, 3.3], 'B': [5.0, 6.1, 7.2]}, index=[2010, 2011, 2012])
    df2 = df.set_index(df.index.astype(np.int32))
    tm.assert_frame_equal(df, df2)