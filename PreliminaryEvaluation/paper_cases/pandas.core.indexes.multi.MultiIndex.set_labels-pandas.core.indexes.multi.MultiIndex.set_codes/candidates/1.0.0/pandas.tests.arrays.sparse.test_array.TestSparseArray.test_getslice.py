def test_getslice(self):
    result = self.arr[:-3]
    exp = SparseArray(self.arr.to_dense()[:-3])
    tm.assert_sp_array_equal(result, exp)
    result = self.arr[-4:]
    exp = SparseArray(self.arr.to_dense()[-4:])
    tm.assert_sp_array_equal(result, exp)
    result = self.arr[-12:]
    exp = SparseArray(self.arr)
    tm.assert_sp_array_equal(result, exp)
    result = self.arr[:-12]
    exp = SparseArray(self.arr.to_dense()[:0])
    tm.assert_sp_array_equal(result, exp)