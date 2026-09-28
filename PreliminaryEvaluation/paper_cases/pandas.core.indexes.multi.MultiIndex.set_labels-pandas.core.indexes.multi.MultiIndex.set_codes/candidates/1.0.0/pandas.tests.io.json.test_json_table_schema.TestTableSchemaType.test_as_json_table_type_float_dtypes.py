@pytest.mark.parametrize('float_dtype', [np.float, np.float16, np.float32, np.float64])
def test_as_json_table_type_float_dtypes(self, float_dtype):
    assert as_json_table_type(float_dtype) == 'number'