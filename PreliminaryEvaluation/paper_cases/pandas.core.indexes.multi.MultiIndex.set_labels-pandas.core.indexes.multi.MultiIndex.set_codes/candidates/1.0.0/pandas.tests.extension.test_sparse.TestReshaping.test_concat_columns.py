def test_concat_columns(self, data, na_value):
    self._check_unsupported(data)
    super().test_concat_columns(data, na_value)