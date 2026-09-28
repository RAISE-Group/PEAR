def test_merge_inner_join_empty(self):
    df_empty = pd.DataFrame()
    df_a = pd.DataFrame({'a': [1, 2]}, index=[0, 1], dtype='int64')
    result = pd.merge(df_empty, df_a, left_index=True, right_index=True)
    expected = pd.DataFrame({'a': []}, index=[], dtype='int64')
    tm.assert_frame_equal(result, expected)