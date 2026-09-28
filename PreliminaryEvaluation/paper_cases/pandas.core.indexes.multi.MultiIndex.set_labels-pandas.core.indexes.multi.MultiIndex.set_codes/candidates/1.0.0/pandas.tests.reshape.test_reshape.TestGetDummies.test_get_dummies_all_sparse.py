def test_get_dummies_all_sparse(self):
    df = pd.DataFrame({'A': [1, 2]})
    result = pd.get_dummies(df, columns=['A'], sparse=True)
    dtype = SparseDtype('uint8', 0)
    expected = pd.DataFrame({'A_1': SparseArray([1, 0], dtype=dtype), 'A_2': SparseArray([0, 1], dtype=dtype)})
    tm.assert_frame_equal(result, expected)