def test_get_indexer_non_unique_dtype_mismatch(self):
    indexes, missing = pd.Index(['A', 'B']).get_indexer_non_unique(pd.Index([0]))
    tm.assert_numpy_array_equal(np.array([-1], dtype=np.intp), indexes)
    tm.assert_numpy_array_equal(np.array([0], dtype=np.int64), missing)