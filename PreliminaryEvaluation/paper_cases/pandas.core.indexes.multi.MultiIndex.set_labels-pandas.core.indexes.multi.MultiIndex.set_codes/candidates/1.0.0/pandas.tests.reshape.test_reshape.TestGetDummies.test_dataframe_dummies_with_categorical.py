def test_dataframe_dummies_with_categorical(self, df, sparse, dtype):
    df['cat'] = pd.Categorical(['x', 'y', 'y'])
    result = get_dummies(df, sparse=sparse, dtype=dtype).sort_index(axis=1)
    if sparse:
        arr = SparseArray
        typ = SparseDtype(dtype, 0)
    else:
        arr = np.array
        typ = dtype
    expected = DataFrame({'C': [1, 2, 3], 'A_a': arr([1, 0, 1], dtype=typ), 'A_b': arr([0, 1, 0], dtype=typ), 'B_b': arr([1, 1, 0], dtype=typ), 'B_c': arr([0, 0, 1], dtype=typ), 'cat_x': arr([1, 0, 0], dtype=typ), 'cat_y': arr([0, 1, 1], dtype=typ)}).sort_index(axis=1)
    tm.assert_frame_equal(result, expected)