def test_merge_take_missing_values_from_index_of_other_dtype(self):
    left = pd.DataFrame({'a': [1, 2, 3], 'key': pd.Categorical(['a', 'a', 'b'], categories=list('abc'))})
    right = pd.DataFrame({'b': [1, 2, 3]}, index=pd.CategoricalIndex(['a', 'b', 'c']))
    result = left.merge(right, left_on='key', right_index=True, how='right')
    expected = pd.DataFrame({'a': [1, 2, 3, None], 'key': pd.Categorical(['a', 'a', 'b', 'c']), 'b': [1, 1, 2, 3]}, index=[0, 1, 2, np.nan])
    expected = expected.reindex(columns=['a', 'key', 'b'])
    tm.assert_frame_equal(result, expected)