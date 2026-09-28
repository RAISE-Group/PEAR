def test_getitem_empty_frame_with_boolean(self):
    df = pd.DataFrame()
    df2 = df[df > 0]
    tm.assert_frame_equal(df, df2)