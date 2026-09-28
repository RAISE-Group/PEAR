@pytest.mark.parametrize('target_add,input_value,expected_value', [('!', ['hello', 'world'], ['hello!', 'world!']), ('m', ['hello', 'world'], ['hellom', 'worldm'])])
def test_string_addition(self, target_add, input_value, expected_value):
    a = Series(input_value)
    result = a + target_add
    expected = Series(expected_value)
    tm.assert_series_equal(result, expected)