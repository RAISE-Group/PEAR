def test_take_negative(self):
    exp = SparseArray(np.take(self.arr_data, [-1]))
    tm.assert_sp_array_equal(self.arr.take([-1]), exp)
    exp = SparseArray(np.take(self.arr_data, [-4, -3, -2]))
    tm.assert_sp_array_equal(self.arr.take([-4, -3, -2]), exp)