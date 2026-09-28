def test_is_not_string_type(self, dtype):
    return not pd.api.types.is_string_dtype(dtype)