def test_encode_with_decimal(self):
    decimal_input = 1.0
    output = ujson.encode(decimal_input)
    assert output == '1.0'