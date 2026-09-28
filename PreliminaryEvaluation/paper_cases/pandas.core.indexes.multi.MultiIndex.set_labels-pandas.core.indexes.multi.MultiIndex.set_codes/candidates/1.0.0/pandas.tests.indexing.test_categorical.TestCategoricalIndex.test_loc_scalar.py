def test_loc_scalar(self):
    result = self.df.loc['a']
    expected = DataFrame({'A': [0, 1, 5], 'B': Series(list('aaa')).astype(CDT(list('cab')))}).set_index('B')
    tm.assert_frame_equal(result, expected)
    df = self.df.copy()
    df.loc['a'] = 20
    expected = DataFrame({'A': [20, 20, 2, 3, 4, 20], 'B': Series(list('aabbca')).astype(CDT(list('cab')))}).set_index('B')
    tm.assert_frame_equal(df, expected)
    with pytest.raises(KeyError, match="^'d'$"):
        df.loc['d']
    msg = 'cannot append a non-category item to a CategoricalIndex'
    with pytest.raises(TypeError, match=msg):
        df.loc['d'] = 10
    msg = 'cannot insert an item into a CategoricalIndex that is not already an existing category'
    with pytest.raises(TypeError, match=msg):
        df.loc['d', 'A'] = 10
    with pytest.raises(TypeError, match=msg):
        df.loc['d', 'C'] = 10
    msg = "cannot do label indexing on <class 'pandas\\.core\\.indexes\\.category\\.CategoricalIndex'> with these indexers \\[1\\] of <class 'int'>"
    with pytest.raises(TypeError, match=msg):
        df.loc[1]