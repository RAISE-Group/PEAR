def test_loc_listlike(self):
    result = self.df.loc[['c', 'a']]
    expected = self.df.iloc[[4, 0, 1, 5]]
    tm.assert_frame_equal(result, expected, check_index_type=True)
    result = self.df2.loc[['a', 'b', 'e']]
    exp_index = CategoricalIndex(list('aaabbe'), categories=list('cabe'), name='B')
    expected = DataFrame({'A': [0, 1, 5, 2, 3, np.nan]}, index=exp_index)
    tm.assert_frame_equal(result, expected, check_index_type=True)
    with pytest.raises(KeyError, match="^'e'$"):
        self.df2.loc['e']
    df = self.df2.copy()
    df.loc['e'] = 20
    result = df.loc[['a', 'b', 'e']]
    exp_index = CategoricalIndex(list('aaabbe'), categories=list('cabe'), name='B')
    expected = DataFrame({'A': [0, 1, 5, 2, 3, 20]}, index=exp_index)
    tm.assert_frame_equal(result, expected)
    df = self.df2.copy()
    result = df.loc[['a', 'b', 'e']]
    exp_index = CategoricalIndex(list('aaabbe'), categories=list('cabe'), name='B')
    expected = DataFrame({'A': [0, 1, 5, 2, 3, np.nan]}, index=exp_index)
    tm.assert_frame_equal(result, expected, check_index_type=True)
    with pytest.raises(KeyError, match="'a list-indexer must only include values that are in the categories'"):
        self.df2.loc[['a', 'd']]