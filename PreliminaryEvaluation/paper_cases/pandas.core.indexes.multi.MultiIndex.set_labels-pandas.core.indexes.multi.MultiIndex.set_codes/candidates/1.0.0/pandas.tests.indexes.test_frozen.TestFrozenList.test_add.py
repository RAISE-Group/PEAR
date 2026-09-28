def test_add(self):
    result = self.container + (1, 2, 3)
    expected = FrozenList(self.lst + [1, 2, 3])
    self.check_result(result, expected)
    result = (1, 2, 3) + self.container
    expected = FrozenList([1, 2, 3] + self.lst)
    self.check_result(result, expected)