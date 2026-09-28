def test_merge_join_different_levels(self):
    df1 = DataFrame(columns=['a', 'b'], data=[[1, 11], [0, 22]])
    columns = MultiIndex.from_tuples([('a', ''), ('c', 'c1')])
    df2 = DataFrame(columns=columns, data=[[1, 33], [0, 44]])
    columns = ['a', 'b', ('c', 'c1')]
    expected = DataFrame(columns=columns, data=[[1, 11, 33], [0, 22, 44]])
    with tm.assert_produces_warning(UserWarning):
        result = pd.merge(df1, df2, on='a')
    tm.assert_frame_equal(result, expected)
    columns = ['a', 'b', ('a', ''), ('c', 'c1')]
    expected = DataFrame(columns=columns, data=[[1, 11, 0, 44], [0, 22, 1, 33]])
    with tm.assert_produces_warning(UserWarning):
        result = df1.join(df2, on='a')
    tm.assert_frame_equal(result, expected)