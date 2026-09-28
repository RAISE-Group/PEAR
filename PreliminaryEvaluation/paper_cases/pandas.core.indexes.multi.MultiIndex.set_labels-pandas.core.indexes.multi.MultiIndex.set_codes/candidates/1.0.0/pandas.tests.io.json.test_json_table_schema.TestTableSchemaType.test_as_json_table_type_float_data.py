@pytest.mark.parametrize('float_type', [np.float, np.float16, np.float32, np.float64])
def test_as_json_table_type_float_data(self, float_type):
    float_data = [1.0, 2.0, 3.0]
    assert as_json_table_type(np.array(float_data, dtype=float_type)) == 'number'