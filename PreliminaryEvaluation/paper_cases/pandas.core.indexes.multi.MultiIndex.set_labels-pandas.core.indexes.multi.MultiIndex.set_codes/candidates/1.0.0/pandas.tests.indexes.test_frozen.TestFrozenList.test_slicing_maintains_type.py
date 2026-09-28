def test_slicing_maintains_type(self):
    result = self.container[1:2]
    expected = self.lst[1:2]
    self.check_result(result, expected)