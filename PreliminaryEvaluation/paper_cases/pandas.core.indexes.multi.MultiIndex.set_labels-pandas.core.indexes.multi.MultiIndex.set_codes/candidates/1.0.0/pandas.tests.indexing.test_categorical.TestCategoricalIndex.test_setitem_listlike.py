def test_setitem_listlike(self):
    np.random.seed(1)
    c = Categorical(np.random.randint(0, 5, size=150000).astype(np.int8)).add_categories([-1000])
    indexer = np.array([100000]).astype(np.int64)
    c[indexer] = -1000
    result = c.codes[np.array([100000]).astype(np.int64)]
    tm.assert_numpy_array_equal(result, np.array([5], dtype='int8'))