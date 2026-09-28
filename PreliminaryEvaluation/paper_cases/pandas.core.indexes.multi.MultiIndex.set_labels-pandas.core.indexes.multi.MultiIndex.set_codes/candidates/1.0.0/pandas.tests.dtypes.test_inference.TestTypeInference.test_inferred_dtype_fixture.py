def test_inferred_dtype_fixture(self, any_skipna_inferred_dtype):
    inferred_dtype, values = any_skipna_inferred_dtype
    assert inferred_dtype == lib.infer_dtype(values, skipna=True)