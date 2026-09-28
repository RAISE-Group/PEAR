def test_dataframe_dummies_all_obj(self, df, sparse):
    df = df[['A', 'B']]
    result = get_dummies(df, sparse=sparse)
    expected = DataFrame({'A_a': [1, 0, 1], 'A_b': [0, 1, 0], 'B_b': [1, 1, 0], 'B_c': [0, 0, 1]}, dtype=np.uint8)
    if sparse:
        expected = pd.DataFrame({'A_a': SparseArray([1, 0, 1], dtype='uint8'), 'A_b': SparseArray([0, 1, 0], dtype='uint8'), 'B_b': SparseArray([1, 1, 0], dtype='uint8'), 'B_c': SparseArray([0, 0, 1], dtype='uint8')})
    tm.assert_frame_equal(result, expected)