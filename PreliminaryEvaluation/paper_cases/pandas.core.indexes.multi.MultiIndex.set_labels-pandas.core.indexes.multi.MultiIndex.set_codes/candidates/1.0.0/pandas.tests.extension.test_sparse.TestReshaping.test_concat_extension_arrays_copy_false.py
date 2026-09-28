def test_concat_extension_arrays_copy_false(self, data, na_value):
    self._check_unsupported(data)
    super().test_concat_extension_arrays_copy_false(data, na_value)