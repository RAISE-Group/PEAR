@pytest.mark.parametrize('int_dtype', [np.int, np.int16, np.int32, np.int64])
def test_as_json_table_type_int_dtypes(self, int_dtype):
    assert as_json_table_type(int_dtype) == 'integer'