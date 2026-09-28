@pytest.mark.parametrize('method,expected', [('pad', np.array([-1, 0, 1, 1], dtype=np.intp)), ('backfill', np.array([0, 0, 1, -1], dtype=np.intp))])
def test_get_indexer_strings(self, method, expected):
    index = pd.Index(['b', 'c'])
    actual = index.get_indexer(['a', 'b', 'c', 'd'], method=method)
    tm.assert_numpy_array_equal(actual, expected)