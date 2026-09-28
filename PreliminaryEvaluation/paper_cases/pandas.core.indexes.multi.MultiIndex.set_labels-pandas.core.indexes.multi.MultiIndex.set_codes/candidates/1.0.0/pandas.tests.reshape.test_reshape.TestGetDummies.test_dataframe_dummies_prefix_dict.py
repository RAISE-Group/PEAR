def test_dataframe_dummies_prefix_dict(self, sparse):
    prefixes = {'A': 'from_A', 'B': 'from_B'}
    df = DataFrame({'C': [1, 2, 3], 'A': ['a', 'b', 'a'], 'B': ['b', 'b', 'c']})
    result = get_dummies(df, prefix=prefixes, sparse=sparse)
    expected = DataFrame({'C': [1, 2, 3], 'from_A_a': [1, 0, 1], 'from_A_b': [0, 1, 0], 'from_B_b': [1, 1, 0], 'from_B_c': [0, 0, 1]})
    columns = ['from_A_a', 'from_A_b', 'from_B_b', 'from_B_c']
    expected[columns] = expected[columns].astype(np.uint8)
    if sparse:
        expected[columns] = expected[columns].astype(pd.SparseDtype('uint8', 0))
    tm.assert_frame_equal(result, expected)