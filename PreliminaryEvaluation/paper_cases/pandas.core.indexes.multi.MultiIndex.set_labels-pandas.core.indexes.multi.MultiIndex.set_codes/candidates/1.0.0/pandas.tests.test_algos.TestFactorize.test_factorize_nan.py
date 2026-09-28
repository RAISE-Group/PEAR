def test_factorize_nan(self):
    key = np.array([1, 2, 1, np.nan], dtype='O')
    rizer = ht.Factorizer(len(key))
    for na_sentinel in (-1, 20):
        ids = rizer.factorize(key, sort=True, na_sentinel=na_sentinel)
        expected = np.array([0, 1, 0, na_sentinel], dtype='int32')
        assert len(set(key)) == len(set(expected))
        tm.assert_numpy_array_equal(pd.isna(key), expected == na_sentinel)
    key = np.array([0, np.nan, 1], dtype='O')
    na_sentinel = -1
    ids = rizer.factorize(key, sort=False, na_sentinel=na_sentinel)
    expected = np.array([2, -1, 0], dtype='int32')
    assert len(set(key)) == len(set(expected))
    tm.assert_numpy_array_equal(pd.isna(key), expected == na_sentinel)