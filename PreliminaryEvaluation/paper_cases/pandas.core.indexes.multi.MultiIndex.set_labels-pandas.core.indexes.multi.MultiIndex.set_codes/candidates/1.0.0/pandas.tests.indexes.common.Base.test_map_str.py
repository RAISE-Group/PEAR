def test_map_str(self):
    index = self.create_index()
    result = index.map(str)
    expected = Index([str(x) for x in index], dtype=object)
    tm.assert_index_equal(result, expected)