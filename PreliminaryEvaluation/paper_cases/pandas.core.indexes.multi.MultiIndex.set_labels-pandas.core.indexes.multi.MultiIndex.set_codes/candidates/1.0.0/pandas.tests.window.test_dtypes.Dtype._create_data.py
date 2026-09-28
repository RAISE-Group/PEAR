def _create_data(self):
    self.data = self._create_dtype_data(self.dtype)
    self.expects = self.get_expects()