def test_dataframe_dummies_drop_first(self, df, sparse):
    df = df[['A', 'B']]
    result = get_dummies(df, drop_first=True, sparse=sparse)
    expected = DataFrame({'A_b': [0, 1, 0], 'B_c': [0, 0, 1]}, dtype=np.uint8)
    if sparse:
        expected = expected.apply(SparseArray, fill_value=0)
    tm.assert_frame_equal(result, expected)