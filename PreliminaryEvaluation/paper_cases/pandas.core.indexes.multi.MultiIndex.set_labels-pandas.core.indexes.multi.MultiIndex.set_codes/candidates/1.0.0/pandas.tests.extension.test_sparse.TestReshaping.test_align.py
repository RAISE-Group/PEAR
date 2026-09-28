def test_align(self, data, na_value):
    self._check_unsupported(data)
    super().test_align(data, na_value)