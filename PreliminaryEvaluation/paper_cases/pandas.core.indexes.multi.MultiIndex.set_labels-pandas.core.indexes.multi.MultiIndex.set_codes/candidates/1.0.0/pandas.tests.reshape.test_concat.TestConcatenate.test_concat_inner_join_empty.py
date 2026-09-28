def test_concat_inner_join_empty(self):
    df_empty = pd.DataFrame()
    df_a = pd.DataFrame({'a': [1, 2]}, index=[0, 1], dtype='int64')
    df_expected = pd.DataFrame({'a': []}, index=[], dtype='int64')
    for how, expected in [('inner', df_expected), ('outer', df_a)]:
        result = pd.concat([df_a, df_empty], axis=1, join=how)
        tm.assert_frame_equal(result, expected)