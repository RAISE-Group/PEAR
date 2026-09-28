def test_unique_na(self):
    idx = pd.Index([2, np.nan, 2, 1], name='my_index')
    expected = pd.Index([2, np.nan, 1], name='my_index')
    result = idx.unique()
    tm.assert_index_equal(result, expected)