def test_combine_first_int(self):
    df1 = pd.DataFrame({'a': [0, 1, 3, 5]}, dtype='int64')
    df2 = pd.DataFrame({'a': [1, 4]}, dtype='int64')
    res = df1.combine_first(df2)
    tm.assert_frame_equal(res, df1)
    assert res['a'].dtype == 'int64'