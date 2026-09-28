def test_categories_assigments(self):
    s = Categorical(['a', 'b', 'c', 'a'])
    exp = np.array([1, 2, 3, 1], dtype=np.int64)
    s.categories = [1, 2, 3]
    tm.assert_numpy_array_equal(s.__array__(), exp)
    tm.assert_index_equal(s.categories, Index([1, 2, 3]))