@pytest.mark.parametrize('bool_dtype', [bool, np.bool])
def test_as_json_table_type_bool_dtypes(self, bool_dtype):
    assert as_json_table_type(bool_dtype) == 'boolean'