def test_is_not_object_type(self, dtype):
    return not pd.api.types.is_object_dtype(dtype)