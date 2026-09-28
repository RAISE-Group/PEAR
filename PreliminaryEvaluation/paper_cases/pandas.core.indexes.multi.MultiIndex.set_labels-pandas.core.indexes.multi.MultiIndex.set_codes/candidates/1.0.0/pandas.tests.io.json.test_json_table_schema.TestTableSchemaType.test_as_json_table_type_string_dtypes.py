@pytest.mark.parametrize('str_dtype', [object])
def test_as_json_table_type_string_dtypes(self, str_dtype):
    assert as_json_table_type(str_dtype) == 'string'