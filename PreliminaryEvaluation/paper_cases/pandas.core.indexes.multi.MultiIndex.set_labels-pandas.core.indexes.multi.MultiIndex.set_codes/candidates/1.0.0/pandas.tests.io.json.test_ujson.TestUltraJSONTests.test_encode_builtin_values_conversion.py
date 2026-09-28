@pytest.mark.parametrize('builtin_value', [None, True, False])
def test_encode_builtin_values_conversion(self, builtin_value):
    output = ujson.encode(builtin_value)
    assert builtin_value == json.loads(output)
    assert output == json.dumps(builtin_value)
    assert builtin_value == ujson.decode(output)