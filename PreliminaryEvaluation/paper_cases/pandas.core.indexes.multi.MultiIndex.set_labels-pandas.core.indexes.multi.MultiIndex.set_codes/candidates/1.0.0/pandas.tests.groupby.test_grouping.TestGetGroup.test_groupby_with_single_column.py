def test_groupby_with_single_column(self):
    df = pd.DataFrame({'a': list('abssbab')})
    tm.assert_frame_equal(df.groupby('a').get_group('a'), df.iloc[[0, 5]])
    exp = pd.DataFrame(index=pd.Index(['a', 'b', 's'], name='a'))
    tm.assert_frame_equal(df.groupby('a').count(), exp)
    tm.assert_frame_equal(df.groupby('a').sum(), exp)
    tm.assert_frame_equal(df.groupby('a').nth(1), exp)