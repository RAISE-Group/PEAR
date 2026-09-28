def setup_method(self, method):
    self.arr_data = np.array([np.nan, np.nan, 1, 2, 3, np.nan, 4, 5, np.nan, 6])
    self.arr = SparseArray(self.arr_data)
    self.zarr = SparseArray([0, 0, 1, 2, 3, 0, 4, 5, 0, 6], fill_value=0)