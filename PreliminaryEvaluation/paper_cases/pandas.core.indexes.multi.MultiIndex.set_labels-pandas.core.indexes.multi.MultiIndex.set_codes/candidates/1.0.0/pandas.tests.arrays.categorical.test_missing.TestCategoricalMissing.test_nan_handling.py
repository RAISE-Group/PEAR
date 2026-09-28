def test_nan_handling(self):
    c = Categorical(['a', 'b', np.nan, 'a'])
    tm.assert_index_equal(c.categories, Index(['a', 'b']))
    tm.assert_numpy_array_equal(c._codes, np.array([0, 1, -1, 0], dtype=np.int8))
    c[1] = np.nan
    tm.assert_index_equal(c.categories, Index(['a', 'b']))
    tm.assert_numpy_array_equal(c._codes, np.array([0, -1, -1, 0], dtype=np.int8))
    c = Categorical(['a', 'b', np.nan, 'a'])
    tm.assert_index_equal(c.categories, Index(['a', 'b']))
    tm.assert_numpy_array_equal(c._codes, np.array([0, 1, -1, 0], dtype=np.int8))