def test_dataframe_dummies_subset(self, df, sparse):
    result = get_dummies(df, prefix=['from_A'], columns=['A'], sparse=sparse)
    expected = DataFrame({'B': ['b', 'b', 'c'], 'C': [1, 2, 3], 'from_A_a': [1, 0, 1], 'from_A_b': [0, 1, 0]}, dtype=np.uint8)
    expected[['C']] = df[['C']]
    if sparse:
        cols = ['from_A_a', 'from_A_b']
        expected[cols] = expected[cols].astype(pd.SparseDtype('uint8', 0))
    tm.assert_frame_equal(result, expected)