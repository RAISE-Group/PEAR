def test_dataframe_dummies_prefix_sep(self, df, sparse):
    result = get_dummies(df, prefix_sep='..', sparse=sparse)
    expected = DataFrame({'C': [1, 2, 3], 'A..a': [1, 0, 1], 'A..b': [0, 1, 0], 'B..b': [1, 1, 0], 'B..c': [0, 0, 1]}, dtype=np.uint8)
    expected[['C']] = df[['C']]
    expected = expected[['C', 'A..a', 'A..b', 'B..b', 'B..c']]
    if sparse:
        cols = ['A..a', 'A..b', 'B..b', 'B..c']
        expected[cols] = expected[cols].astype(pd.SparseDtype('uint8', 0))
    tm.assert_frame_equal(result, expected)
    result = get_dummies(df, prefix_sep=['..', '__'], sparse=sparse)
    expected = expected.rename(columns={'B..b': 'B__b', 'B..c': 'B__c'})
    tm.assert_frame_equal(result, expected)
    result = get_dummies(df, prefix_sep={'A': '..', 'B': '__'}, sparse=sparse)
    tm.assert_frame_equal(result, expected)