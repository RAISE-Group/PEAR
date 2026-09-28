def test_union(self):
    result = self.container.union((1, 2, 3))
    expected = FrozenList(self.lst + [1, 2, 3])
    self.check_result(result, expected)