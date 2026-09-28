def test_left_merge_na_buglet(self):
    left = DataFrame({'id': list('abcde'), 'v1': randn(5), 'v2': randn(5), 'dummy': list('abcde'), 'v3': randn(5)}, columns=['id', 'v1', 'v2', 'dummy', 'v3'])
    right = DataFrame({'id': ['a', 'b', np.nan, np.nan, np.nan], 'sv3': [1.234, 5.678, np.nan, np.nan, np.nan]})
    result = merge(left, right, on='id', how='left')
    rdf = right.drop(['id'], axis=1)
    expected = left.join(rdf)
    tm.assert_frame_equal(result, expected)