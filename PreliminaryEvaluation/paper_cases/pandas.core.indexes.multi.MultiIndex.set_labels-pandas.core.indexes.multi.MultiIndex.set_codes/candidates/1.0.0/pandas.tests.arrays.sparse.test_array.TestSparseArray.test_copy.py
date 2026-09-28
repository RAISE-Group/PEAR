def test_copy(self):
    arr2 = self.arr.copy()
    assert arr2.sp_values is not self.arr.sp_values
    assert arr2.sp_index is self.arr.sp_index