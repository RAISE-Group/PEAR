def test_constructor_copy(self):
    cp = SparseArray(self.arr, copy=True)
    cp.sp_values[:3] = 0
    assert not (self.arr.sp_values[:3] == 0).any()
    not_copy = SparseArray(self.arr)
    not_copy.sp_values[:3] = 0
    assert (self.arr.sp_values[:3] == 0).all()