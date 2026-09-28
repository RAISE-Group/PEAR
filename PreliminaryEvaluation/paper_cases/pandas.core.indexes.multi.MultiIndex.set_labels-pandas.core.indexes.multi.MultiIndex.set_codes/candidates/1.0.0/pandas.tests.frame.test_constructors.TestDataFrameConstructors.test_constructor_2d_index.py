def test_constructor_2d_index(self):
    df = pd.DataFrame([[1]], columns=[[1]], index=[1, 2])
    expected = pd.DataFrame([1, 1], index=pd.Int64Index([1, 2], dtype='int64'), columns=pd.MultiIndex(levels=[[1]], codes=[[0]]))
    tm.assert_frame_equal(df, expected)
    df = pd.DataFrame([[1]], columns=[[1]], index=[[1, 2]])
    expected = pd.DataFrame([1, 1], index=pd.MultiIndex(levels=[[1, 2]], codes=[[0, 1]]), columns=pd.MultiIndex(levels=[[1]], codes=[[0]]))
    tm.assert_frame_equal(df, expected)