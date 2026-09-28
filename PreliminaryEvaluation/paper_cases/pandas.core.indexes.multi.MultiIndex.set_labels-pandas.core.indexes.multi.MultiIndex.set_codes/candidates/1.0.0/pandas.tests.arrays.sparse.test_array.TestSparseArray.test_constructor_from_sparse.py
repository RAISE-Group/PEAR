def test_constructor_from_sparse(self):
    res = SparseArray(self.zarr)
    assert res.fill_value == 0
    tm.assert_almost_equal(res.sp_values, self.zarr.sp_values)