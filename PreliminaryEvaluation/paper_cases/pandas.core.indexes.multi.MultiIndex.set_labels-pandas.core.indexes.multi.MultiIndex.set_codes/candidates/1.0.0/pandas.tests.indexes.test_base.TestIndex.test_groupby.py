def test_groupby(self):
    index = Index(range(5))
    result = index.groupby(np.array([1, 1, 2, 2, 2]))
    expected = {1: pd.Index([0, 1]), 2: pd.Index([2, 3, 4])}
    tm.assert_dict_equal(result, expected)