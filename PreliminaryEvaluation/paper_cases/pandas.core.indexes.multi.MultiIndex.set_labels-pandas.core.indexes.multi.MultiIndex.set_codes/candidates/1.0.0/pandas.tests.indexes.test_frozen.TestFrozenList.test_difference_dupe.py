def test_difference_dupe(self):
    result = FrozenList([1, 2, 3, 2]).difference([2])
    expected = FrozenList([1, 3])
    self.check_result(result, expected)