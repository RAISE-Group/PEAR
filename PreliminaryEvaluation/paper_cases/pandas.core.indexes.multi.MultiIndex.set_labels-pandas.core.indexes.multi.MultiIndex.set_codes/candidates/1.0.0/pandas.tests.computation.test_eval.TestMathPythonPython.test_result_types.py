def test_result_types(self):
    self.check_result_type(np.int32, np.float64)
    self.check_result_type(np.int64, np.float64)
    self.check_result_type(np.float32, np.float32)
    self.check_result_type(np.float64, np.float64)