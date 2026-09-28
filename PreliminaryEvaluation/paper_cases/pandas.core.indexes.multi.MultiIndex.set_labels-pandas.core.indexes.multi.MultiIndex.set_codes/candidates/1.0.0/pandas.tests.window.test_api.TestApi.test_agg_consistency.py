def test_agg_consistency(self):
    df = DataFrame({'A': range(5), 'B': range(0, 10, 2)})
    r = df.rolling(window=3)
    result = r.agg([np.sum, np.mean]).columns
    expected = pd.MultiIndex.from_product([list('AB'), ['sum', 'mean']])
    tm.assert_index_equal(result, expected)
    result = r['A'].agg([np.sum, np.mean]).columns
    expected = Index(['sum', 'mean'])
    tm.assert_index_equal(result, expected)
    result = r.agg({'A': [np.sum, np.mean]}).columns
    expected = pd.MultiIndex.from_tuples([('A', 'sum'), ('A', 'mean')])
    tm.assert_index_equal(result, expected)