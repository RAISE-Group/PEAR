@pytest.mark.parametrize('str_data', [pd.Series(['a', 'b']), pd.Index(['a', 'b'])])
def test_as_json_table_type_string_data(self, str_data):
    assert as_json_table_type(str_data) == 'string'