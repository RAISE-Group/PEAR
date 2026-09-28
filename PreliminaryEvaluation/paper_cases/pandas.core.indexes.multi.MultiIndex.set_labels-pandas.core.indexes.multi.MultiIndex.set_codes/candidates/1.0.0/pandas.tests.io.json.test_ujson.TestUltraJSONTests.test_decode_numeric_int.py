@pytest.mark.parametrize('numeric_int_as_str', ['31337', '-31337'])
def test_decode_numeric_int(self, numeric_int_as_str):
    assert int(numeric_int_as_str) == ujson.decode(numeric_int_as_str)