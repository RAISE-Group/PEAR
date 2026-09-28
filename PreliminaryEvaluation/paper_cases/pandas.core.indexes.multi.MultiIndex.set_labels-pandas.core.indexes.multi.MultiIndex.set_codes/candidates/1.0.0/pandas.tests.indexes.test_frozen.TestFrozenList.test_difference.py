def test_difference(self):
    result = self.container.difference([2])
    expected = FrozenList([1, 3, 4, 5])
    self.check_result(result, expected)