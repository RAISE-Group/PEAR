def test_dataframe_dummies_prefix_str(self, df, sparse):
    result = get_dummies(df, prefix='bad', sparse=sparse)
    bad_columns = ['bad_a', 'bad_b', 'bad_b', 'bad_c']
    expected = DataFrame([[1, 1, 0, 1, 0], [2, 0, 1, 1, 0], [3, 1, 0, 0, 1]], columns=['C'] + bad_columns, dtype=np.uint8)
    expected = expected.astype({'C': np.int64})
    if sparse:
        expected = pd.concat([pd.Series([1, 2, 3], name='C'), pd.Series([1, 0, 1], name='bad_a', dtype='Sparse[uint8]'), pd.Series([0, 1, 0], name='bad_b', dtype='Sparse[uint8]'), pd.Series([1, 1, 0], name='bad_b', dtype='Sparse[uint8]'), pd.Series([0, 0, 1], name='bad_c', dtype='Sparse[uint8]')], axis=1)
    tm.assert_frame_equal(result, expected)