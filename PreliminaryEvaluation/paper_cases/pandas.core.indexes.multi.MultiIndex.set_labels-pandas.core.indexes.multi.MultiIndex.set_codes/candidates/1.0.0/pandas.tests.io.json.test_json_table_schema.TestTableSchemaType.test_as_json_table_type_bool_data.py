@pytest.mark.parametrize('bool_type', [bool, np.bool])
def test_as_json_table_type_bool_data(self, bool_type):
    bool_data = [True, False]
    assert as_json_table_type(np.array(bool_data, dtype=bool_type)) == 'boolean'