def test_join_hierarchical_mixed(self):
    df = DataFrame([(1, 2, 3), (4, 5, 6)], columns=['a', 'b', 'c'])
    new_df = df.groupby(['a']).agg({'b': [np.mean, np.sum]})
    other_df = DataFrame([(1, 2, 3), (7, 10, 6)], columns=['a', 'b', 'd'])
    other_df.set_index('a', inplace=True)
    with tm.assert_produces_warning(UserWarning):
        result = merge(new_df, other_df, left_index=True, right_index=True)
    assert ('b', 'mean') in result
    assert 'b' in result