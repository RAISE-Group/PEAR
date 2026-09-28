def test_union_noncomparable(self):
    index = self.create_index()
    other = Index([datetime.now() + timedelta(i) for i in range(4)], dtype=object)
    result = index.union(other)
    expected = Index(np.concatenate((index, other)))
    tm.assert_index_equal(result, expected)
    result = other.union(index)
    expected = Index(np.concatenate((other, index)))
    tm.assert_index_equal(result, expected)