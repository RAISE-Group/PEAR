def test_get_dummies_duplicate_columns(self, df):
    df.columns = ['A', 'A', 'A']
    result = get_dummies(df).sort_index(axis=1)
    expected = DataFrame([[1, 1, 0, 1, 0], [2, 0, 1, 1, 0], [3, 1, 0, 0, 1]], columns=['A', 'A_a', 'A_b', 'A_b', 'A_c'], dtype=np.uint8).sort_index(axis=1)
    expected = expected.astype({'A': np.int64})
    tm.assert_frame_equal(result, expected)