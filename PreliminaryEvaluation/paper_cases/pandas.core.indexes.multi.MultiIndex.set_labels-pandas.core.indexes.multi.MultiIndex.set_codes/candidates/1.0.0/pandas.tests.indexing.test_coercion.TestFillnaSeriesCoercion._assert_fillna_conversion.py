def _assert_fillna_conversion(self, original, value, expected, expected_dtype):
    """ test coercion triggered by fillna """
    target = original.copy()
    res = target.fillna(value)
    self._assert(res, expected, expected_dtype)