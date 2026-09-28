@pytest.mark.parametrize('int_type', [np.int, np.int16, np.int32, np.int64])
def test_as_json_table_type_int_data(self, int_type):
    int_data = [1, 2, 3]
    assert as_json_table_type(np.array(int_data, dtype=int_type)) == 'integer'