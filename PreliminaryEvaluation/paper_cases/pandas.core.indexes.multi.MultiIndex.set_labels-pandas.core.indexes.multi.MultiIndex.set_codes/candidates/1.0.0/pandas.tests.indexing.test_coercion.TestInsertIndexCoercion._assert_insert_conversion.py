def _assert_insert_conversion(self, original, value, expected, expected_dtype):
    """ test coercion triggered by insert """
    target = original.copy()
    res = target.insert(1, value)
    tm.assert_index_equal(res, expected)
    assert res.dtype == expected_dtype