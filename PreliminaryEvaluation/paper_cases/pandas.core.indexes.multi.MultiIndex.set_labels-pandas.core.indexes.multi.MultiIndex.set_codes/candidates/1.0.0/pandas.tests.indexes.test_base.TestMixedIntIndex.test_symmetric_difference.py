def test_symmetric_difference(self):
    index = self.create_index()
    first = index[:4]
    second = index[3:]
    result = first.symmetric_difference(second)
    expected = Index([0, 1, 2, 'a', 'c'])
    tm.assert_index_equal(result, expected)