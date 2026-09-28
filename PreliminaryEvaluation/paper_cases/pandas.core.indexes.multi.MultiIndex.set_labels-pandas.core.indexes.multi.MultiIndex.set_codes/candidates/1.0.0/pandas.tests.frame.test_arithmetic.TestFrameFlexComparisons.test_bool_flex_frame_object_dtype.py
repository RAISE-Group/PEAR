def test_bool_flex_frame_object_dtype(self):
    df1 = pd.DataFrame({'col': ['foo', np.nan, 'bar']})
    df2 = pd.DataFrame({'col': ['foo', datetime.now(), 'bar']})
    result = df1.ne(df2)
    exp = pd.DataFrame({'col': [False, True, False]})
    tm.assert_frame_equal(result, exp)