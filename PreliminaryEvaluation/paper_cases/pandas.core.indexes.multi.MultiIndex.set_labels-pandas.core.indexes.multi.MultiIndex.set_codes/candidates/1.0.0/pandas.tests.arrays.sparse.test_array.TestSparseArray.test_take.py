def test_take(self):
    exp = SparseArray(np.take(self.arr_data, [2, 3]))
    tm.assert_sp_array_equal(self.arr.take([2, 3]), exp)
    exp = SparseArray(np.take(self.arr_data, [0, 1, 2]))
    tm.assert_sp_array_equal(self.arr.take([0, 1, 2]), exp)