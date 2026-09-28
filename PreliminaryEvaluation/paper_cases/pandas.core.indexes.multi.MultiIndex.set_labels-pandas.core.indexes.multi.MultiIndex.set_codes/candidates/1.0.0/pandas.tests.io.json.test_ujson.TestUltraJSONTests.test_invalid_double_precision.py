@pytest.mark.parametrize('invalid_val', [20, -1, '9', None])
def test_invalid_double_precision(self, invalid_val):
    double_input = 30.123456789012344
    expected_exception = ValueError if isinstance(invalid_val, int) else TypeError
    with pytest.raises(expected_exception):
        ujson.encode(double_input, double_precision=invalid_val)