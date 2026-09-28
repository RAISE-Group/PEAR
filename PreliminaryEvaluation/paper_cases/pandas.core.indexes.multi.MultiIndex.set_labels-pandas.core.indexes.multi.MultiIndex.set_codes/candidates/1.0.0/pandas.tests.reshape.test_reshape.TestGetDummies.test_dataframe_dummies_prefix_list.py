def test_dataframe_dummies_prefix_list(self, df, sparse):
    prefixes = ['from_A', 'from_B']
    result = get_dummies(df, prefix=prefixes, sparse=sparse)
    expected = DataFrame({'C': [1, 2, 3], 'from_A_a': [1, 0, 1], 'from_A_b': [0, 1, 0], 'from_B_b': [1, 1, 0], 'from_B_c': [0, 0, 1]}, dtype=np.uint8)
    expected[['C']] = df[['C']]
    cols = ['from_A_a', 'from_A_b', 'from_B_b', 'from_B_c']
    expected = expected[['C'] + cols]
    typ = SparseArray if sparse else pd.Series
    expected[cols] = expected[cols].apply(lambda x: typ(x))
    tm.assert_frame_equal(result, expected)