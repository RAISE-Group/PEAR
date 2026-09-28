def _assert_where_conversion(self, original, cond, values, expected, expected_dtype):
    """ test coercion triggered by where """
    target = original.copy()
    res = target.where(cond, values)
    self._assert(res, expected, expected_dtype)