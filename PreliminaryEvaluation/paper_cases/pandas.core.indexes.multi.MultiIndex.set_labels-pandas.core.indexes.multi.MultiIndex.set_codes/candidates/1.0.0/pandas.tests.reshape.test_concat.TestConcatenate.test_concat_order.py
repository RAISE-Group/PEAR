def test_concat_order(self):
    dfs = [pd.DataFrame(index=range(3), columns=['a', 1, None])]
    dfs += [pd.DataFrame(index=range(3), columns=[None, 1, 'a']) for i in range(100)]
    result = pd.concat(dfs, sort=True).columns
    expected = dfs[0].columns
    tm.assert_index_equal(result, expected)