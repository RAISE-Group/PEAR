def test_loc_ax_single_level_indexer_simple_df(self):
    df = pd.DataFrame(np.arange(9).reshape(3, 3), columns=['a', 'b', 'c'])
    result = df.loc(axis=1)['a']
    expected = pd.Series(np.array([0, 3, 6]), name='a')
    tm.assert_series_equal(result, expected)