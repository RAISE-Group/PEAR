def test_values_asarray(self):
    tm.assert_almost_equal(self.arr.to_dense(), self.arr_data)