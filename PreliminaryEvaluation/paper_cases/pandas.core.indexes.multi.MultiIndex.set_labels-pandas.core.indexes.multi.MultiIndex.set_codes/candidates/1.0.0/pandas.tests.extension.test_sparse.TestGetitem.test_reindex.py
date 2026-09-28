def test_reindex(self, data, na_value):
    self._check_unsupported(data)
    super().test_reindex(data, na_value)