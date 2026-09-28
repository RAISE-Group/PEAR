def test_merge(self, data, na_value):
    self._check_unsupported(data)
    super().test_merge(data, na_value)