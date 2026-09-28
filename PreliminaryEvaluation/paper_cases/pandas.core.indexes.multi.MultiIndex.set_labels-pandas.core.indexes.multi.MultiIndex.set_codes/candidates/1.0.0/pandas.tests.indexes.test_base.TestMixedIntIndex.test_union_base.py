def test_union_base(self):
    index = self.create_index()
    first = index[3:]
    second = index[:5]
    result = first.union(second)
    expected = Index([0, 1, 2, 'a', 'b', 'c'])
    tm.assert_index_equal(result, expected)