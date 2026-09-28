def test_intersection(self):
    index = self.create_index()
    other = Index([1, 2, 3, 4, 5])
    result = index.intersection(other)
    expected = Index(np.sort(np.intersect1d(index.values, other.values)))
    tm.assert_index_equal(result, expected)
    result = other.intersection(index)
    expected = Index(np.sort(np.asarray(np.intersect1d(index.values, other.values))))
    tm.assert_index_equal(result, expected)