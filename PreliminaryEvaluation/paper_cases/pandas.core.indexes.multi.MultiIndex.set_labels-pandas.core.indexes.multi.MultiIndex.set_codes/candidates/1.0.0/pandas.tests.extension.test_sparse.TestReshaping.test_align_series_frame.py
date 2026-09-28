def test_align_series_frame(self, data, na_value):
    self._check_unsupported(data)
    super().test_align_series_frame(data, na_value)